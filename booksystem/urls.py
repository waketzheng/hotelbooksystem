from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from backend.views import about, index, order, order_done, room_info


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', about),
    url(r'^roominfo/', room_info),
    url(r'^$', index, name='home'),
    url(r'^order/', order),
    url(r'^order/done/', order_done)
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns + staticfiles_urlpatterns() + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    ) + [
        # path('favicon.ico', RedirectView.as_view(url='/m/favicon.ico')),
    ]
else:
    from qiniuyun import views as qiniu_views
    urlpatterns += [
        url(r'^upload/$', qiniu_views.upload, name='upload'),
        url(r'^upload/done/$', qiniu_views.upload_result, name='upload_done'),
        url(r'^images/$', qiniu_views.show_imgs, name='show_imgs'),
    ]
