from django.forms import forms


def validate_f_word(content):
    if "fuck" in content.lower():
        raise forms.ValidationError("Can't tweet F word!")
    return content
