from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from .views import Content, Vote, SpecificContent, Comment, Update, Create

app_name = 'status'

urlpatterns = [
        url(r'^content/$', Content.as_view(), name='content'),

        url(r'^vote/$', Vote.as_view(), name='vote'),

        url(r'^comment/$', Comment.as_view(), name='comment'),

        url(r'^status/$', SpecificContent.as_view(), name='specific'),
        url(r'^create/$',Create.as_view(), name='create'),

        url(r'^update/(?P<type>[a-z]+)/$', Update.as_view(), name='update'),

        ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
