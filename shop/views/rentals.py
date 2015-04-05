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

    items = hmod.Product.objects.all()

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

    return templater.render_to_response(request, 'rentals.html', params)
