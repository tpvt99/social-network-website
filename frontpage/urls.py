# urls

from django.conf.urls import url

# view
from .views import FrontPage
from .views import LogForm, RegForm
from .views import Register, Login, Logout

app_name = 'frontpage'

urlpatterns = [
        url(r'^$',FrontPage.as_view(), name='frontpage'),
        url(r'^logform/$', LogForm.as_view(), name='logform'),
        url(r'^regform/$', RegForm.as_view(), name='regform'),

        url(r'^register/$', Register.as_view(), name='register'),

        url(r'^login/$', Login.as_view(), name='login'),

        url(r'^logout/$', Logout.as_view(), name='logout'),


        ]
