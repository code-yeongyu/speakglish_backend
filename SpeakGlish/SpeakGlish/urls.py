from django.contrib import admin
from django.conf.urls import url, include
from api import views as ServerView
from account import views as AccountView
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^api/', include('api.urls'))
]
urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += [
    url(r'^auth/', include('account.urls')),
    url(r'^admin', admin.site.urls)
]