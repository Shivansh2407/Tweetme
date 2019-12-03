from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegisterForm(forms.Form):
    username = forms.CharField(label='User Name')
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password_confirm != password:
            raise forms.ValidationError("Passwords don't match!")
        return password_confirm

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError('This user name has already been taken!')

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('This email has already been used!')

        return email
