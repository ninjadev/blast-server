# MEMEBLAST

## Komme i gang

virtualenv memeblast && cd memeblast && source bin/activate
git clone git@bitbucket.org:sigveseb/memeblast.git && cd memeblast
cp memeblast/memeblast/settings.py.example memeblast/memeblast/settings.py
pip install -r requirements_dev.txt
python manage.py migrate


## Advarsler

Ingen må slette settings.py i git, da dør prodskriptet :P

## Nyttige kommandoer

### Starte utviklingsserver

    python manage.py runserver

### Migrere databaseendringer

    python manage.py migrate

### Lage nye migreringer etter modellendringer

    python manage.py makemigrations

### deploy til server
 
    fab deploy
