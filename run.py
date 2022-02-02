# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_migrate import Migrate
from sys import exit
from decouple import config

import csv
from sqlalchemy.orm.mapper import configure_mappers

from apps.home.models import Data
from apps.config import config_dict
from apps import create_app, db

# WARNING: Don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

# The configuration
get_config_mode = 'Debug' if DEBUG else 'Production'

try:

    # Load the configuration using the default values
    app_config = config_dict[get_config_mode.capitalize()]

except KeyError:
    exit('Error: Invalid <config_mode>. Expected values [Debug, Production] ')

app = create_app(app_config)
Migrate(app, db)

if DEBUG:
    app.logger.info('DEBUG       = ' + str(DEBUG))
    app.logger.info('Environment = ' + get_config_mode)
    app.logger.info('DBMS        = ' + app_config.SQLALCHEMY_DATABASE_URI)


@app.cli.command("load_data")
def load_data():
    """
       Reset and Init database with new sample
       from 'media/transactions_data.csv' file in 'Data' model.
    """
    
    # Create Tables (if not exist)
    db.create_all()

    # Truncate 
    db.session.query(Data).delete()
    db.session.commit()

    with open('media/transactions_data.csv', newline='') as csvfile:
        
        csvreader = csv.reader(csvfile) # load file
        header    = next(csvreader)     # ignore header (1st line)
        
        for row in csvreader:
            _data = Data(type=row[2], name=row[0], value=row[1])
            db.session.add(_data)

        db.session.commit()

if __name__ == "__main__":
    app.run()
