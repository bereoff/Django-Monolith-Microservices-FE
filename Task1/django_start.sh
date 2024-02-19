#!/bin/bash


# Applying database migrations
echo " "
echo "Applying database migrations ..."
python manage.py migrate

# Starting server ...
echo " "
echo " Starting server ..."
python manage.py runserver
