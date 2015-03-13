from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.conf import settings
import django.contrib.auth
from homepage.models import SiteUser
import homepage.models as hmod
from django.core import validators
from django.forms import fields, util
from django.core import exceptions
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django_mako_plus.controller.router import MakoTemplateRenderer
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.hashers import UNUSABLE_PASSWORD_PREFIX, identify_hasher
from collections import OrderedDict
from collections import OrderedDict

templater = get_renderer('shop')

###################################### PROCESS REQUEST ######################################
@view_function
@login_required(login_url='/homepage/login/')
def process_request(request):


    params = {}

    return templater.render_to_response(request, 'account.html', params)



###################################### EDIT USER ######################################
@view_function
def edit(request):
    params = {}


    user = hmod.SiteUser.objects.get(id=request.user.id)

    form = UserEditForm(initial={
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
    })

    if request.method == 'POST':
        form = UserEditForm(request.POST)
        form.userid = user.id
        if form.is_valid():
            user.username = form.cleaned_data['username']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()

            return HttpResponse('''
                <script>
                    window.location.href = window.location.href;
                </script>
            ''')

    params['form'] = form

    return templater.render_to_response(request, 'account.edit.html', params)

class UserEditForm(forms.Form):
    username = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_username(self):
        user_count = hmod.SiteUser.objects.filter(username=self.cleaned_data['username']).exclude(id=self.userid).count()
        if user_count >= 1:
            raise forms.ValidationError("Username already exists.")

        return self.cleaned_data['username']




###################################### CHANGE PASSWORD ######################################
@view_function
def changepassword(request):
    params = {}


    user = hmod.SiteUser.objects.get(id=request.user.id)

    form = PasswordChangeForm(user)
    if request.method == 'POST':
        form = PasswordChangeForm(user, data = request.POST)
        if form.is_valid():

            form.save()
            update_session_auth_hash(request, form.user)

            return HttpResponse('''
                <script>
                    window.location.href = window.location.href;
                </script>
            ''')

    params['form'] = form
    print("passing bad form")
    return templater.render_to_response(request, 'account.changepassword.html', params)
    
