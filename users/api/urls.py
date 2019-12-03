from django.conf.urls import url

from .views import FollowToggleAPIView

urlpatterns = [
    url(r'^(?P<username>[\w.@+-]+)/follow-toggle/$', FollowToggleAPIView.as_view(), name='follow-toggle'),
]
