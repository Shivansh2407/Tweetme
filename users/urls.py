from django.conf.urls import url, include

from .views import UserDetailView

urlpatterns = [
    url(r'^(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name='detail'),
]