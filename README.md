hotelbooksystem
===============

A demo for hotel order booking system


Base on
-------

Python: 3.8+

Django: 4.0+

MySQL

Debug
------

1. clone source and cd to the project

```bash
git clone https://github.com/waketzheng/hotelbooksystem
cd hotelbooksystem
```

2. create a virtual environment(use `poetry`: https://github.com/python-poetry/poetry)

```bash
poetry install --no-root
```

3. activate it

```bash
poetry shell
```

4. init database

```bash
(venv)$ python manage.py migrate
(venv)$ python manage.py loaddata fixtures/romanload_hotel.json
```

5. run server

```bash
(venv)$ python manage.py runserver
```

6. open the url at webbrowser

    http://127.0.0.1:8000/


Production
-------------

1. configure settings, database and email

```bash
echo '
DEBUG=0
DB_USER=your-database-user-name
DB_PASSWD=your-database-password
EMAIL=your-email
EMAIL_PASSWD=your-email-password
' > .env
```

Example of `.env`:
```
DEBUG=0
DB_USER=root
DB_PASSWD=123456
EMAIL=waketzheng@gmail.com
EMAIL_PASSWD=123456
```

2. create virtual environment and activate it

```bash
poetry install --no-root --no-dev
poetry shell
```

3. create database for this project and migrate

```bash
./scripts/createdatabase.py
```

4. deploy as other django project

    https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/gunicorn/
