# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import request
from flask_restx import Api, Resource, fields

from apps import db
from apps.home.models import Data
from apps.api import rest_api

"""
API Interface:
   
   - /data
       - GET: return all items
       - POST: create a new item
   
   - /data/:id
       - GET    : get item
       - PUT    : update item
       - DELETE : delete item
"""

"""
Flask-RestX models Request & Response DATA
"""

# Used to validate input data for creation
create_model = rest_api.model('CreateModel', {"value": fields.String(required=True, min_length=1, max_length=255)})

# Used to validate input data for update
update_model = rest_api.model('UpdateModel', {"value": fields.String(required=True, min_length=1, max_length=255)})

"""
    Flask-Restx routes
"""

@rest_api.route('/api/data')
class Items(Resource):

    """
       Return all items
    """
    def get(self):

        items = Data.query.all()
        
        return {"success" : True,
                "msg"     : "Items found ("+ str(len( items ))+")",
                "datas"   : str( items ) }, 200

    """
       Create new item
    """
    @rest_api.expect(create_model, validate=True)
    def post(self):

        # Read ALL input  
        req_data = request.get_json()

        # Get the information    
        item_value = req_data.get("value")

        # Create new object
        new_item = Data(value=item_value)

        # Save the data
        new_item.save()
        
        return {"success": True,
                "msg"    : "Item successfully created ["+ str(new_item.id)+"]"}, 200

@rest_api.route('/api/data/<int:id>')
class ItemManager(Resource):

    """
       Return Item
    """
    def get(self, id):

        item = Data.get_by_id(id)

        if not item:
            return {"success": False,
                    "msg": "Item not found."}, 400

        return {"success" : True,
                "msg"     : "Successfully return item [" +str(id)+ "]",
                "data"    :  item.toJSON()}, 200

    """
       Update Item
    """
    @rest_api.expect(update_model, validate=True)
    def put(self, id):

        item = Data.get_by_id(id)

        if not item:
            return {"success": False,
                    "msg": "Item not found."}, 400

        # Read input from body  
        req_data = request.get_json()

        # Get the information    
        item_val = req_data.get("value")


        item.update_value(item_val)
        item.save()

        return {"success" : True,
                "msg"     : "Item [" +str(id)+ "] successfully updated",
                "data"    :  item.toJSON()}, 200 

    """
       Delete Item
    """
    def delete(self, id):

        # Locate the Item
        item = Data.get_by_id(id)

        if not item:
            return {"success": False,
                    "msg": "Item not found."}, 400

        # Delete and save the change
        Data.query.filter_by(id=id).delete()
        db.session.commit()

        return {"success" : True,
                "msg"     : "Item [" +str(id)+ "] successfully deleted"}, 200                           
