"""tweetme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from users.views import UserRegisterView
from tweets.views import TweetListSkeleton

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TweetListSkeleton.as_view(), name='home'),
    url(r'^tweets/', include(('tweets.urls', 'tweets'),namespace='tweets')),
    url(r'^api/tweets/', include(('tweets.api.urls','tweets.api.urls'), namespace='tweet-api')),
    url(r'^api/users/', include(('users.api.urls','users.api.urls'), namespace='user-api')),
    #url(r'^.well-known/', include(('letsencrypt.urls','letsencrypt.urls'),namespace='letsencrypt')),
    url(r'^register/$', UserRegisterView.as_view(), name='register'),
    url(r'^all/$', TweetListSkeleton.as_view(), name='all'),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^', include(('users.urls','users.urls'), namespace='users')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
