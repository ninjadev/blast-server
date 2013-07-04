# MEMEBLAST

## Komme i gang

virtualenv memeblast && cd memeblast && source bin/activate
git clone git@bitbucket.org:sigveseb/memeblast.git && cd memeblast
cp memeblast/memeblast/settings.py.example memeblast/memeblast/settings.py
pip install -r requirements_dev.txt
python manage.py syncdb --migrate


## Advarsler

Ingen må slette settings.py i git, da dør prodskriptet :P

## Nyttige kommandoer

### Starte utviklingsserver

    python manage.py runserver

### Migrere databaseendringer

    python manage.py syncdb --migrate

### Lage nye migreringer etter modellendringer

    python manage.py schemamigration <appname> --auto

### deploy til server
 
    fab deploy
