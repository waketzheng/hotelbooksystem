from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView

from qiniuyun import views as qiniuyun_views
from backend.viewspackage.aboutView import about
from backend.viewspackage.indexView import index
from backend.viewspackage.orderResultView import orderResult
from backend.viewspackage.orderView import order
from backend.viewspackage.roomInfoView import roomInfo


urlpatterns = [
    url(r'^upload/$', qiniuyun_views.upload, name='upload'),
    url(r'^upload/done/$', qiniuyun_views.upload_result, name='upload_done'),
    url(r'^images/$', qiniuyun_views.show_imgs, name='show_imgs'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', about),
    url(r'^roominfo/', roomInfo),
    url(r'^$', index, name='home'),
    url(r'^order/', order),
    url(r'^orderresult/', orderResult)
]

