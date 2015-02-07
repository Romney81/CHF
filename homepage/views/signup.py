from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
import django.contrib.auth
from django.contrib.auth.models import Group
from django.contrib.auth import login
import homepage.models as hmod
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
    user = hmod.SiteUser()
    group = Group.objects.get(name="Guppies")

    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
           user.username = form.cleaned_data['username']
           user.first_name = form.cleaned_data['first_name']
           user.last_name = form.cleaned_data['last_name']
           user.email = form.cleaned_data['email']
           user.set_password( form.cleaned_data['password2'] )
           user.save()

           return HttpResponseRedirect('/homepage/login/')

    params['form'] = form
    return templater.render_to_response(request, 'signup.html', params)

class UserCreationForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.CharField(required=True, max_length=30,widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password1'}))
    password2 = forms.CharField(required=True, max_length=30,widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password2'}))
