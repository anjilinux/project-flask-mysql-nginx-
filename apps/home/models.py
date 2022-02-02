# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from datetime import datetime

from apps import db

class Data(db.Model):

    __tablename__ = 'data'

    id = db.Column(db.Integer, primary_key=True)

    type   = db.Column(db.String(64))
    name   = db.Column(db.String(64))
    value  = db.Column(db.Integer)
    ts     = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return str( self.id ) 

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update_value(self, new_value):
        self.value = new_value

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def toDICT(self):

        cls_dict          = {}
        cls_dict['_id']   = self.id
        cls_dict['name'] = self.name
        cls_dict['value'] = self.value

        return cls_dict

    def toJSON(self):

        return self.toDICT()
