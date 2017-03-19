from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from .views import MessageView, Ajax, CreateMessAjax

app_name = 'message'

urlpatterns = [

        url(r'^ajax/$', Ajax.as_view(), name='ajax'),

        url(r'^message/$', MessageView.as_view(), name='message'),

        url(r'^ajax_create/$', CreateMessAjax.as_view(), name='ajaxcreate'),

        ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
