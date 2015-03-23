# BLAST
Persistent social image sharing feed for the whole world.

## Installing

```
virtualenv blast && cd blast && source bin/activate 
git clone git@github.com:ninjadev/blast-server.git && cd blast-server 
cp blast/settings/settings.py.example blast/settings/settings.py 
pip install -r requirements_dev.txt 
python manage.py migrate 
```


### Warning
Do not delete settings.py from  git, as the prod script then will die.

## Commands

### Start development server

    python manage.py runserver

### Migrate database changes

    python manage.py migrate

### Create new migrations or model changes

    python manage.py makemigrations

### Deploy to server
 
    fab deploy
