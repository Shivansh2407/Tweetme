from django.forms import forms
from django.forms.utils import ErrorList


class FormUserNeededMixin(object):
    def form_valid(self, form):
        if self.request.user.is_authenticated():
            form.instance.user = self.request.user
            return super(FormUserNeededMixin, self).form_valid(form)
        else:
            form._errors[forms.NON_FIELD_ERRORS] = ErrorList(['User must be logged in to continue!'])
            return self.form_invalid(form)


class UserOwnerMixin(object):
    def form_valid(self, form):
        if form.instance.user == self.request.user:
            return super(UserOwnerMixin, self).form_valid(form)
        else:
            form._errors[forms.NON_FIELD_ERRORS] = ErrorList(["Can't modify others' tweet!"])
            return self.form_invalid(form)