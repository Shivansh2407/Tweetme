from django.conf import settings
from django.db import models
from django.urls import reverse

from .validators import validate_f_word


class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.deletion.CASCADE)
    content = models.CharField(max_length=140, validators=[validate_f_word])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.content)

    def get_absolute_url(self):
        return reverse('tweets:detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ['-created_at']
