# Dependencies

    apt-get install python3 python3-pip libsasl2-dev
    pip3 install -r requirements.txt

## Optional dependencies

    bpython3

# Running the server

## Generating the database

First, generate the migration file:

    python manage.py makemigrations

Then, create the db.sqlite3 file using this migration:

    python manage.py migrate

## Running the server

Once you have the db.sqlite3 file, you are ready to run the server:

    python manage.py runserver
