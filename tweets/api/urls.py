from django.conf.urls import url

from .views import TweetListAPIView, TweetCreateAPIView, TweetListAllAPIView, TweetDestroyAPIView

urlpatterns = [
    url(r'^$', TweetListAPIView.as_view(), name='list'),
    url(r'^all/$', TweetListAllAPIView.as_view(), name='all'),
    url(r'^create/$', TweetCreateAPIView.as_view(), name='create'),
    url(r'^(?P<username>[\w.@+-]+)/$', TweetListAPIView.as_view(), name='user-tweets'),
    url(r'^(?P<pk>\d+)/delete/$', TweetDestroyAPIView.as_view(), name='delete'),
]
