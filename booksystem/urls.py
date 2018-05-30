from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from backend.views import about, index, order, order_done, room_info


urlpatterns = [
    path("admin/", admin.site.urls),
    path("about/", about, name="abount"),
    path("roominfo/", room_info, name="room-info"),
    path("", index, name="home"),
    path("order/", order, name="order"),
    path("order/done/", order_done, name="order-done"),
]

if settings.DEBUG:
    # django debug toolbar
    import debug_toolbar

    urlpatterns.insert(0, path("__debug__/", include(debug_toolbar.urls)))

    # static and media
    urlpatterns += staticfiles_urlpatterns() + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
