# Shipwreck Inspector

This Django app is for managing shipwreck data, for the Maritime Archaeological Association of Western Australia.
It holds interconnected data on:
- sites
- reports (site visits)
- publications
- people
- projects

It is designed for public access, with members given the ability to add/edit information.

Created by Patrick Morrison, Feb 2022

## Installation

Setup like any django app. It can use sqlite, so doesn't need postgres locally. When in the directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Usage

TBC

## Deploy to Heroku
This app is configured with a procfile and django-heroku to deploy easily. Simply point Heroku to the git repository, add a postgres database and run it. You will then need to run:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

## License
[MIT](https://choosealicense.com/licenses/mit/)