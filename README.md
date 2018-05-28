hotelbooksystem
===============

A demo for hotel order booking system

<br />

# Base on

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

2. modify `.env`, DB_USER -- database user, DB_PASSWD -- database password

```bash
vi .env
```
3. create virtualenv environment(use `pipenv`: https://docs.pipenv.org/)

```bash
# You may need to install gcc zlib-dev python3-dev mysql-dev
# see: https://github.com/PyMySQL/mysqlclient-python
pipenv install --dev
```

4. activate virtualenv

```bash
pipenv shell
```

5. init database

```bash
(venv)$ python manage.py migrate
(venv)$ python manage.py loaddata fixtures/init_hotel_name_and_pic.json
```

7. run server

```bash
(venv)$ python manage.py runserver
```

8. open the url at webbrowser

    http://127.0.0.1:8000/

Optional: use qiniu for static and image file server
-----------

7. 修改其中的配置（数据库、邮箱和七牛云)
```
vi booksystem/local_settings.py
```
10. 登录管理员，然后再进入上传页面：

http://127.0.0.1:8000/admin

http://127.0.0.1:8000/upload

11. 上传图片到七牛云存储（七牛上需有local_settings.py中对应的私有空间）：
- 图片在static/pic
- Name输入框需留空
- 一个个来并且全部上传

Production
-------------

1. configure settings of database

```bash
echo '
dB_USER = your-database-user-name
DB_PASSWD = your-database-password
' > .env
```

2. deploy as other django project

    https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/gunicorn/
