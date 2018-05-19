from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from backend.views import about, index, order, order_done, room_info


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about, name='abount'),
    path('roominfo/', room_info, name='room-info'),
    path('', index, name='home'),
    path('order/', order, name='order'),
    path('order/done/', order_done, name='order-done')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns + staticfiles_urlpatterns() + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
else:
    from qiniuyun import views as qiniu_views
    urlpatterns += [
        path('upload/', qiniu_views.upload, name='upload'),
        path('upload/done/', qiniu_views.upload_result, name='upload_done'),
        path('images/', qiniu_views.show_imgs, name='show_imgs'),
    ]
