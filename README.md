# BLAST
Persistent social image sharing feed for the whole world.

## Installing

```
virtualenv blast && cd blast && source bin/activate 
git clone git@github.com:ninjadev/blast-server.git && cd blast-server 
cp blast/settings/settings.py.example blast/settings/settings.py 
make
```


### Warning
Do not delete settings.py from git, as the prod script then will die.

## Commands

### Start development server

    make run

### Migrate database changes

    make migrate

### Create new migrations or model changes

    make migrations

### Update dependencies

    make update

### Deploy to server

    fab deploy
