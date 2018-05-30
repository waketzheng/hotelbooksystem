from .base import *

ALLOWED_HOSTS = ["127.0.0.1"]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "hotelbooksystem",  # 数据库里的database名称
        "USER": os.environ.get("DB_USER", "root"),
        "PASSWORD": os.environ.get("DB_PASSWD", "123456"),
        "HOST": "127.0.0.1",
        "PORT": 3306,
        "OPTIONS": {"charset": "utf8mb4"},
    }
}


#  Email ,ref:http://www.cnblogs.com/BeginMan/p/3443158.html

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"  # email后端
EMAIL_HOST_USER = os.environ.get("EMAIL")  # 发送邮件的邮箱地址
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASSWD")  # 发送邮件的邮箱密码
_smtp = EMAIL_HOST_USER.split("@")[-1].lower()
_type = _smtp.split(".")[-2]
EMAIL_USE_TLS = False  # 是否使用TLS安全传输协议
EMAIL_USE_SSL = _type in ("qq",)  # 是否使用SSL加密，qq企业邮箱要求使用，网易邮箱则不需要
EMAIL_HOST = f"smtp.{_smtp}"  # 发送邮件的邮箱 的 SMTP服务器
EMAIL_PORT = 465 if _type in ("qq",) else 25  # 发件箱的SMTP服务器端口
DEFAULT_FROM_EMAIL = os.environ.get("EMAIL")  # 这项可要可不要
