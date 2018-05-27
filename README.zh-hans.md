======================
# hotelbooksystem
======================

基于Django的python信息管理系统，用于酒店预订管理

<br />

# Base on

Python: 3.6

Django: 2.0+

MySQL

debug:
------

1. 克隆项目：
```
git clone https://github.com/waketzheng/hotelbooksystem
```
2. 进入文件夹：
```
cd hotelbooksystem
```
3. 修改.env文件中的DB_USER,DB_PASSWD
```
vi .env
```
4. 建立虚拟环境：
```
# You may need to install gcc zlib-dev python3-dev mysql-dev
# see: https://github.com/PyMySQL/mysqlclient-python
pipenv install --dev
```
5. 激活虚拟环境：
```
pipenv shell
```
6. 初始化数据（首次运行）：
```
(venv)$ python manage.py migrate
(venv)$ python manage.py loaddata fixtures/init_hotel_name_and_pic.json
```
7. 运行服务：
```
(venv)$ python manage.py runserver
```
8. 打开如下网址即可看到运行效果：

http://127.0.0.1:8000/

production:
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
