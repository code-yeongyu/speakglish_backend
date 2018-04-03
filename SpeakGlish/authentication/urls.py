from django.conf.urls import url
from rest_framework.authtoken import views as drf_views
from authentication import views

urlpatterns = [
    url(r'^login/$', drf_views.obtain_auth_token, name='auth'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'username/$', views.change_username, name='change_username'),
    url(r'^password/$', views.change_password, name='change_password')
]