from api import views as ServerView
from django.conf.urls import url

urlpatterns = [
    url(r'^articles/$', ServerView.ArticleList.as_view()),
    url(r'^articles/(?P<pk>[0-9]+)/$', ServerView.ArticleDetail.as_view()),
    url(r'^profile/', ServerView.user_profile),
    url(r'^signup/', ServerView.signup)
]