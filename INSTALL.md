# Dependencies

D'abord, installez `python3` et `pip`:

    # Sous une Debian-like
    apt-get install python3 python3-pip libsasl2-dev

    # Sous Archlinux
    pacman -S python python-pip libsasl # et si vous préférez l'installer avec pacman, python-django

Puis utilisez `pip` pour télécharger les paquets python nécessaires:

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
