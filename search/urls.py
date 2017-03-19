#urls

from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

#view
from .views import Search
from .views import InstanceSearch
from .views import ActivityContent, AllContent
from .views import UserContent
from .views import Image

app_name = 'search'

urlpatterns= [ 
    url(r'^(?P<field>[a-z]+)/$', Search.as_view(), name='search'),

    url(r'^isearch/(?P<field>[a-z]+)/$', InstanceSearch.as_view(), name='instancesearch'),

    url(r'^activity/content/$', ActivityContent.as_view(), name='activity_content'),

    url(r'^all/content/$', AllContent.as_view(), name='all_content'),

    url(r'^user/content/$', UserContent.as_view(), name='user_content'),

    url(r'ajax/image/(?P<field>[0-9]+)/$', Image.as_view(), name='image'),

    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
