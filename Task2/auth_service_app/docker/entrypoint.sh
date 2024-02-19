#!/bin/bash

FLAG_FILE="{$PWD}/check_migr.txt"

# Function to check and execute commands
run_commands() {
    if [ -f "$FLAG_FILE" ] && [ "$(cat $FLAG_FILE)" == "true" ]; then
        echo "Flag is true. Skipping makemigrations."
        python manage.py migrate
        python manage.py collectstatic --no-input
    else
        echo "Flag is not set or false. Running makemigrations."
        python manage.py makemigrations
        python manage.py migrate
        python manage.py collectstatic --no-input

        # Creates the flag file
        echo "true" > "$FLAG_FILE"
    fi
}

# Checks and executes the commands
run_commands

exec "$@"

