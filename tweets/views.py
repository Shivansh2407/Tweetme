from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.views.generic import DetailView, UpdateView, TemplateView

from users.models import UserProfile
from .mixins import UserOwnerMixin
from .forms import TweetModelForm
from .models import Tweet


class TweetListSkeleton(TemplateView):
    """
    Only provide page skeleton, do the listing by Ajax afterward.
    """
    template_name = "tweets/home.html"

    def get_context_data(self, **kwargs):
        context = super(TweetListSkeleton, self).get_context_data(**kwargs)
        context['create_form'] = TweetModelForm()
        context['users_data'] = [{
            'user': user,
            'is_following': UserProfile.custom_objects.is_following(self.request.user, user),
        } for user in get_user_model().objects.annotate(tweet_count=Count('tweet')).order_by('-tweet_count')]

        return context


class TweetDetail(DetailView):
    model = Tweet
    template_name = "tweets/detail.html"

    def get_context_data(self, **kwargs):
        context = super(TweetDetail, self).get_context_data(**kwargs)
        context['is_following'] = UserProfile.custom_objects.is_following(self.request.user, self.get_object().user)
        return context


class TweetUpdate(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    model = Tweet
    form_class = TweetModelForm
    template_name = "tweets/update.html"
