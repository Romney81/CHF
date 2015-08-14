from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
import django.contrib.auth
from django.contrib.auth import login
from django.contrib.auth.models import Group
import homepage.models as hmod
from homepage.models import SiteUser
from django.core import validators
from django.forms import fields, util
from django.core import exceptions
from django_mako_plus.controller.router import MakoTemplateRenderer
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer

templater = get_renderer('shop')

######################## main view function ########################
@view_function
def process_request(request):
    params = {}

    event = hmod.Event.objects.get(id = request.urlparams[0])
    areas = hmod.Area.objects.all()
    items = hmod.Item.objects.all()

    params['event'] = event
    params['areas'] = areas
    params['items'] = items
    return templater.render_to_response(request, 'event_details.html', params)