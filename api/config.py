#!/usr/bin/python
import os

AIRBNB_ENV = os.environ.get('AIRBNB_ENV')
AIRBNB_DATABASE_PWD_DEV = os.environ.get('AIRBNB_DATABASE_PWD_DEV')
AIRBNB_DATABASE_PWD_PROD = os.environ.get('AIRBNB_DATABASE_PWD_PROD')

if (AIRBNB_ENV == "development"):
    DEBUG = True
    HOST = "localhost"
    PORT = 3333
    DATABASE = {
        'host': '158.69.92.190',
        'user': 'airbnb_user_dev',
        'database': 'airbnb_dev',
        'port': '3306',
        'charset': 'utf8',
        'password': 'AIRBNB_DATABASE_PWD_DEV'
    }
elif (AIRBNB_ENV == "production"):
    DEBUG = False
    HOST = "0.0.0.0"
    PORT = 3000
    DATABASE = {
        'host': '158.69.92.190',
        'user': 'airbnb_user_prod',
        'database': 'airbnb_prod',
        'port': '3306',
        'charset': 'utf8',
        'password': 'AIRBNB_DATABASE_PWD_DEV'
