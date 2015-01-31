from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
import django.contrib.auth
from homepage import models
from homepage.models import SiteUser
from django.core import validators
from django.forms import fields, util
from django.core import exceptions
from django_mako_plus.controller.router import MakoTemplateRenderer
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer

templater = get_renderer('homepage')

@view_function
def process_request(request):
	'''This function is used to validate username and password
	when users log in to the system. Specifically, it will 
	create a form and authenticate against the database
	'''
	
	

	# prepare the login form
	form = LoginForm()
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			django.contrib.auth.login(request, form.user)
			return HttpResponseRedirect('/homepage/manager/')    

	template_vars = {
		'form': form,
	}

	return templater.render_to_response(request, 'login.html', template_vars)


class LoginForm(forms.Form):
	'''This is a Django login form'''

	username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
	password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

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
def logout(request):
	# check user permissions and prepare the params
	params = prepare_params(request, require_authenticated=False)

	django.contrib.auth.logout(request)
	request.session.flush()
	
	return HttpResponseRedirect('/homepage/login/')