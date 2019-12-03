from django import forms

from .models import Tweet


class TweetModelForm(forms.ModelForm):
    content = forms.CharField(label='',
                              widget=forms.Textarea(
                                  attrs={'placeholder': "What's happening?",
                                         "class": "form-control",
                                         'rows': 3}
                              ))

    class Meta:
        model = Tweet
        fields = [
            'content'
        ]
