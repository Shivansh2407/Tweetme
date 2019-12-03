from django.utils.timesince import timesince
from rest_framework import serializers

from tweets.models import Tweet

from users.api.serializers import UserDisplaySerializer


class TweetModelSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True)
    time_since = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()

    class Meta:
        model = Tweet
        fields = [
            'user',
            'content',
            'time_since',
            'url'
        ]

    def get_time_since(self, tweet):
        return timesince(tweet.created_at)

    def get_url(self, tweet):
        return tweet.get_absolute_url()
