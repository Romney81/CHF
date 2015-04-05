from django import forms
from django.contrib.auth.forms import PasswordResetForm
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
import django.contrib.auth
from django.contrib.auth.tokens import default_token_generator
from homepage import models
from homepage.models import SiteUser
from django.core import validators
from django.forms import fields, util
from django.core import exceptions
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template import loader
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.views.generic import *
from django.contrib import messages
from django_mako_plus.controller.router import MakoTemplateRenderer
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer

templater = get_renderer('homepage')

@view_function
def process_request(request):

	#prepare the login form
	form = UserForgotPasswordForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save(from_email = 'romney81@gmail.com', email_template_name= 'password_reset_email.html', use_https = False, token_generator = default_token_generator, html_email_template_name=None)



	template_vars = {
		'form': form,
	}

	return templater.render_to_response(request, 'password_reset_request.html', template_vars)

class UserForgotPasswordForm(PasswordResetForm):
	email = forms.EmailField(required=True,max_length=254)


@view_function
def change(request):

	params = {}


    #user = hmod.SiteUser.objects.get(id=request.user.id)

	form = newpassword()
    # if request.method == 'POST':
    #     form = PasswordChangeForm(user, data = request.POST)
    #     if form.is_valid():
	#
    #         form.save()
    #         update_session_auth_hash(request, form.user)
	#
    #         return HttpResponse('''
    #             <script>
    #                 window.location.href = window.location.href;
    #             </script>
    #         ''')

	params['form'] = form
	return templater.render_to_response(request, 'password_reset_request.change.html', params)

class newpassword(forms.Form):
	new_password1 = forms.CharField(label=("New password"),
	                                widget=forms.PasswordInput)
	new_password2 = forms.CharField(label=("New password confirmation"),
	                                widget=forms.PasswordInput)
