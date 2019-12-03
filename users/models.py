from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse

class UserProfileManager(models.Manager):
    def toggle_follow(self, user, user_to_toggle):
        profile = self.get(user=user)
        if user_to_toggle in profile.following.all():
            profile.following.remove(user_to_toggle)
            is_following = False
        else:
            profile.following.add(user_to_toggle)
            is_following = True
        return is_following

    def is_following(self, user, user_for_following):
        if not user.is_authenticated:
            return False
        profile = self.get(user=user)
        return user_for_following in profile.following.all()


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile',on_delete=models.deletion.CASCADE)
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='followed_by')

    custom_objects = UserProfileManager()

    def __str__(self):
        return '%s(following %d user(s))' % (self.user.username, self.following.all().count())

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.user.username})


def post_save_user_receiver(sender, instance, created, **kwargs):
    if created:
        UserProfile.custom_objects.create(user=instance)

post_save.connect(post_save_user_receiver, sender=settings.AUTH_USER_MODEL)
