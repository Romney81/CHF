from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
import django.contrib.auth
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
    now = datetime.datetime.now()
    user = hmod.Artisan()

    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
           user.username = form.cleaned_data['username']
           user.set_password( form.cleaned_data['password2'] )
           user.start_year = now.strftime('%Y-%m-%d')
           user.trade = ''
           user.bio = ''
           user.save()
           return HttpResponseRedirect('/homepage/index/')

    params['form'] = form
    return templater.render_to_response(request, 'signup.html', params)

class UserCreationForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1=forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2=forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
