#urls 

from django.conf.urls import url

# views

from .views import AddFriend, FriendAjax
from .views import FriendRequest, Search


app_name = 'friend'

urlpatterns = [
        url(r'^add/$', AddFriend.as_view(), name='addfriend'),

        url(r'^request/$', FriendRequest.as_view(), name='request'),

        url(r'^search/$', Search.as_view(), name='search'),

        url(r'^friendajax/$', FriendAjax.as_view(), name='ajax'),
        ]

