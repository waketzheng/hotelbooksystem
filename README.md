hotelbooksystem
===============

A demo for hotel order booking system


Base on
-------

Python: 3.6

Django: 2.0+

MySQL

Debug
------

1. clone source and cd to the project

```bash
git clone https://github.com/waketzheng/hotelbooksystem
cd hotelbooksystem
```

2. create a virtual environment(use `pipenv`: https://docs.pipenv.org/)

```bash
# You may need to install gcc zlib-dev python3-dev mysql-dev
# see: https://github.com/PyMySQL/mysqlclient-python
pipenv install --dev
```

3. activate it

```bash
pipenv shell
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
DJANGO_SETTINGS_MODULE=booksystem.settings.prod
dB_USER=your-database-user-name
DB_PASSWD=your-database-password
EMAIL=your-email
EMAIL_PASSWD=your-email-password
' > .env
```

Example of `.env`:
```
DJANGO_SETTINGS_MODULE=booksystem.settings.prod
dB_USER=root
DB_PASSWD=123456
EMAIL=jaket5219999@126.com
EMAIL_PASSWD=123456
```

2. create virtual environment and activate it

```bash
pipenv install
pipenv shell
```

3. create database for this project and migrate

```bash
./scripts/createdatabase.py
```

4. deploy as other django project

    https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/gunicorn/

Optional: use qiniu for static and image file server
-----------

5. configure database, email and qiniu
```bash
vi booksystem/local_settings.py
```
6. login as admin to upload images

    http(s)://your-domain-or-ip/admin

    http(s)://your-domain-or-ip/upload

7. upload images to qiniu(should have private storage at qiniu at configure keys at settings/prod.py)
