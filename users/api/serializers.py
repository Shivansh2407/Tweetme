from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.serializers import ModelSerializer, SerializerMethodField

User = get_user_model()


class UserDisplaySerializer(ModelSerializer):
    follower_count = SerializerMethodField()
    url = SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'follower_count',
            'url'
        ]

    def get_follower_count(self, user):
        return 0

    def get_url(self, user):
        return reverse('users:detail', kwargs={'username': user.username})
