from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
import django.contrib.auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Group
from homepage import models
import homepage.models as hmod
from homepage.models import SiteUser
from django.core import validators
from django.forms import fields, util
from django.core import exceptions
from django_mako_plus.controller.router import MakoTemplateRenderer
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

templater = get_renderer('shop')

######################## main view function ########################
@view_function
def process_request(request):


    params = {}

    items = hmod.Item.objects.all()

    # item_ids = request.session['shopping_cart']
    #
    # countitems = []
    #
    # for ids in item_ids:
    #     item = hmod.Item.objects.get(id = ids)
    #     countitems.append(item)
    #
    #
    # template_vars['countitems'] = len(countitems)

    params['items'] = items

    return templater.render_to_response(request, 'index.html', params)


######################## loginform view request ########################
@view_function
def loginform(request):
    #prepare the login form
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            django.contrib.auth.login(request, form.user)

            return HttpResponse('''
                <script>
                    window.location.href = window.location.href;
                </script>
            ''')


    template_vars = {
      'form': form,
    }

    return templater.render_to_response(request, 'index.loginform.html', template_vars)

######################## Loing Form Class ########################
class LoginForm(forms.Form):
	username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
	password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

	# These below functions are used to display error messages for incorrect
	# user name and password. Notice clean_(name) must match the field name.

	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')

		self.user = django.contrib.auth.authenticate(username=username, password=password)
		if self.user == None:
			raise forms.ValidationError('Incorrect username/password.')

		return self.cleaned_data


@view_function
def registerform(request):
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
            return HttpResponse('''
               <script>
                   window.location.href = window.location.href;
               </script>
           ''')

    params['form'] = form
    return templater.render_to_response(request, 'index.registerform.html', params)
class MyUserCreationForm(forms.Form):
    error_messages = {
        'duplicate_username': ("A user with that username already exists."),
        'password_mismatch': ("The two password fields didn't match."),
    }
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    password1 = forms.CharField(required=True, max_length=30,widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password1'}))
    password2 = forms.CharField(required=True, max_length=30,widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password2'}))

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


@view_function
def search(request):

    params = {}

    searchfor = request.REQUEST.get('input')

    items = []
    if searchfor != '':
        if request.method == 'POST':
            items = hmod.Item.objects.filter(name = searchfor)
    else:
        items = hmod.Item.objects.all()


    params['items'] = items

    return templater.render_to_response(request, 'index.search.html', params)
