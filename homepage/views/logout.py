from django import forms
from django.contrib.auth import logout
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
import django.contrib.auth
from homepage import models
from django.core import validators
from django.forms import fields, util
from django.core import exceptions
from django_mako_plus.controller.router import MakoTemplateRenderer
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer

templater = get_renderer('homepage')

@view_function
def process_request(request):
	template_vars = {
	}
	django.contrib.auth.logout(request)
	return templater.render_to_response(request, 'index.html', template_vars)
	
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/homepage/index/')
	  




