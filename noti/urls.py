from django.conf.urls import url
from .views import NotiAjax
from django.conf import settings
from django.conf.urls.static import static

app_name = 'noti'

urlpatterns = [

        url(r'^notiajax/$', NotiAjax.as_view(), name='notiajax'),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
