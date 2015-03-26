.PHONY: all
all: update migrate

.PHONY: migrate
migrate:
	python manage.py migrate

.PHONY: update
update:
	pip install -r requirements_dev.txt

.PHONY: run
run:
	python manage.py runserver

.PHONY: migrations
migrations:
	python manage.py makemigrations
