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

templater = get_renderer('homepage')

######################## main view function ########################
@view_function
def process_request(request):


    #empty params
    params = {}

    #get all events
    events = hmod.Event.objects.all()

    #month and day lists
    month = []
    day = []

    #for loop to get month and day
    for event in events:
        newmonth = event.start_date.strftime('%b')
        newday = event.start_date.strftime('%d')
        month.append(newmonth)
        day.append(newday)

    #pass event, month and day to festivals.html
    params['months'] = month
    params['days'] = day
    params['events'] = events

    return templater.render_to_response(request, 'festivals.html', params)
