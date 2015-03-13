from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
import django.contrib.auth
from django.contrib.auth.models import Group
from django.contrib.auth import login, authenticate
import homepage.models as hmod
from homepage.models import SiteUser
from django.core import validators
from django.forms import fields, util
from django.core import exceptions
from django_mako_plus.controller.router import MakoTemplateRenderer
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
import datetime

templater = get_renderer('homepage')

@view_function
def process_request(request):
    params = {}

    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = SiteUser()
            user.username = form.cleaned_data['username']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.set_password( form.cleaned_data['password2'] )
            user.save()

            #login user after authentication
            user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password2'])
            login(request, user)

            return HttpResponseRedirect('/shop/')

    params['form'] = form
    return templater.render_to_response(request, 'signup.html', params)

class MyUserCreationForm(forms.Form):
        error_messages = {
            'duplicate_username': ("A user with that username already exists."),
            'password_mismatch': ("The two password fields didn't match."),
        }
        username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
        first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
        last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
        password1 = forms.CharField(required=True, max_length=30,widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
        password2 = forms.CharField(required=True, max_length=30,widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Confirmation'}))

        def clean_username(self):
            username = self.cleaned_data["username"]
            try:
                SiteUser._default_manager.get(username=username)
            except SiteUser.DoesNotExist:
                return username
            raise forms.ValidationError(
                self.error_messages['duplicate_username'],
                code='duplicate_username',
            )

        def clean_password2(self):
            password1 = self.cleaned_data.get("password1")
            password2 = self.cleaned_data.get("password2")
            if password1 and password2 and password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
            return password2
