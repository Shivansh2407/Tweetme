from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.urls import reverse_lazy
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import UserProfile

User = get_user_model()


class FollowToggleAPIView(APIView):
    def get(self, request, format=None, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect(reverse_lazy('login'))
        user_to_toggle = User.objects.get(username=kwargs['username'])
        is_following = UserProfile.custom_objects.toggle_follow(self.request.user, user_to_toggle)
        followed_by_ids = user_to_toggle.followed_by.values_list('user_id', flat=True)
        return Response({
            'username': user_to_toggle.username,
            'is_following': is_following,
            'followed_by': [{
                'username': username,
                'url': reverse_lazy('users:detail', kwargs={'username': username})
            } for username in User.objects.filter(id__in=followed_by_ids).values_list('username', flat=True)]
        })
