from django.conf.urls import url
from django.views.generic import RedirectView

from .views import TweetListSkeleton, TweetDetail, TweetUpdate

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/')),
    url(r'^search/$', TweetListSkeleton.as_view(), name='search'),
    url(r'^(?P<pk>\d+)/$', TweetDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', TweetUpdate.as_view(), name='update'),
]