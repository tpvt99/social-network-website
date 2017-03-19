#urls 

from django.conf.urls import url

# view
from .views import ActivityView

app_name = 'vote'

urlpatterns = [
        url(r'^vote/(?P<field>[a-z]+)/+$', ActivityView.as_view(), name='vote'),
        ]
