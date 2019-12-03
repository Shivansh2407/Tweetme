from django.contrib.auth import get_user_model, login
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView

from .models import UserProfile
from .forms import UserRegisterForm

User = get_user_model()


class UserDetailView(DetailView):
    model = User
    template_name = 'users/detail.html'

    def get_object(self, queryset=None):
        return get_object_or_404(User, username__iexact=self.kwargs.get('username'))

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['is_following'] = UserProfile.custom_objects.is_following(self.request.user, self.get_object())
        return context


class UserRegisterView(FormView):
    form_class = UserRegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        new_user = User.objects.create_user(username, email, password)
        login(self.request, new_user)

        return super(UserRegisterView, self).form_valid(form)
