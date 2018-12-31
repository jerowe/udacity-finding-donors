#!/usr/bin/env bash


#export HOUSING_DATA='/Users/jillian/Dropbox/classes/udacity-machine-learning/boston-house-prices/flask_app/materials/housing.csv'
#gunicorn --workers=2 --bind=0.0.0.0:5000 --keep-alive=2000 --timeout=2000 --log-level=debug flask_app:flask_app --daemon
export DONOR_DATA='/Users/jillian/Dropbox/classes/udacity-machine-learning/finding-donors/finding-donors-flask-app/materials/census.csv'
gunicorn --workers=2 --bind=0.0.0.0:5000 --keep-alive=2000 --timeout=2000 --log-level=debug flask_app:app
