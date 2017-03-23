from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import Post

app_name = 'image'


urlpatterns = [
    url(r'^post/$', Post.as_view(), name='post'),
        ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
