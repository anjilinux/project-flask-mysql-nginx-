# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_migrate import Migrate
from sys import exit
from decouple import config

import csv
from datetime import datetime
from random   import randint
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


# Inner command 
def load_cmd(aUseRandomValues=None):

    if aUseRandomValues:
        print( ' >>> Randomize Values ')
    else:
        print( ' >>> Use Values from input file ')

    # Create Tables (if not exist)
    db.create_all()

    # Truncate 
    db.session.query(Data).delete()
    db.session.commit()

    with open('media/transactions_data.csv', newline='') as csvfile:
        
        csvreader = csv.reader(csvfile) # load file
        header    = next(csvreader)     # ignore header (1st line)
        
        '''
        Expected format: 
            HEADER: product_code,product_info,value,currency,type
            SAMPLE: Lenovo_Ideapad_3i, Lenovo Ideapad 3i 14.0inch FHD Laptop,9.5,euro,transaction
            
            product_code (string)  : Lenovo_Ideapad_3i
            product_info (string)  : Lenovo Ideapad 3i 14.0inch FHD Laptop
            value        (integer) : 9 
            currency     (string)  : usd, eur 
            type         (string)  : transaction (hardoded)
        '''

        iter = 0 # used for timestamp
        for row in csvreader:

            iter += 1

            if len( row ) != 5:
                print( ' >>> Error parsing line ('+str(iter)+') -> ' + ' '.join([str(elem) for elem in row]) )
                continue        

            item_code     = row[0]
            item_name     = row[1]

            if aUseRandomValues:
                item_value = randint(5, 100)
            else:
                item_value = row[2]

            item_currency = row[3]
            item_type     = row[4]

            # randomize in the past the transaction date
            # The distribuition range ~1 month 
            item_ts       = datetime.utcnow().timestamp() - ( 2 * iter * randint(5, 10) * 3600 )
            item_ts       = int( item_ts )

            _data = Data(code=item_code, name=item_name, value=item_value, currency=item_currency, type=item_type, ts=item_ts)

            db.session.add(_data)

        db.session.commit()

@app.cli.command("load_data")
def load_data():

    return load_cmd()

@app.cli.command("load_random_data")
def load_data():

    return load_cmd( True )

@app.template_filter('ctime')
def timectime(s):
    return datetime.utcfromtimestamp( s ).strftime('%Y-%m-%d')

if __name__ == "__main__":
    app.run()
