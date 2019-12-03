from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Tweet


User = get_user_model()  


class TweetModelTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="James Ho")

    def test_tweet_item(self):
        tweet = Tweet.objects.create(
            user=User.objects.first(),
            content='whatever~~'
        )
        self.assertTrue(tweet.user.username == 'James Ho')

    def test_tweet_url(self):
        tweet = Tweet.objects.create(
            user=User.objects.first(),
            content='whatever~~'
        )
        self.assertEqual(tweet.get_absolute_url(), reverse('tweets:detail', kwargs={'pk': tweet.id}))
