#!/bin/bash

#Set env variables
echo POSTGRES_DB=$POSTGRES_DB >> .env
echo POSTGRES_USER=$POSTGRES_USER >> .env
echo POSTGRES_PASSWORD=$POSTGRES_PASSWORD >> .env
echo POSTGRES_HOST=$POSTGRES_HOST >> .env
echo POSTGRES_PORT=$POSTGRES_PORT >> .env
echo SECRET_KEY=$SECRET_KEY >> .env


# Collect static files
echo "Makemigrations"
python manage.py makemigrations

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:80