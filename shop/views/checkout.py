from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
import django.contrib.auth
from django.contrib.auth import login
from django.contrib.auth.models import Group
from homepage import models
from homepage.models import SiteUser
from django.core import validators
from django.forms import fields, util
from django.core import exceptions
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django_mako_plus.controller.router import MakoTemplateRenderer
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
import homepage.models as hmod

templater = get_renderer('shop')

######################## main view function ########################
@view_function
@login_required(login_url='/homepage/login/')
def process_request(request):


    params = {}

    item_ids = request.session['shopping_cart']

    items = {}

    for key,value in item_ids.items():

        item = hmod.Item.objects.get(id = key)

        item_container = []
        item_container.append(item)
        item_container.append(value)

        items[item.id] = item_container

    form = checkoutForm()

    print(items)
    params['items'] = items
    params['form'] = form
    return templater.render_to_response(request, 'checkout.html', params)


class checkoutForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))
    email = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    phone = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primary Phone'}))
    address = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Address'}))
    country = forms.ChoiceField(widget = forms.Select(attrs={'class': 'form-control'}), choices=([('1','United States'), ('2','Canada'),('3','Mexico'), ]))

    state = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}))
    city = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}))

@view_function
def confirmation(request):
    params = {}

    item_ids = request.session['shopping_cart']

    items = {}

    for key,value in item_ids.items():

        item = hmod.Item.objects.get(id = key)

        item_container = []
        item_container.append(item)
        item_container.append(value)

        items[item.id] = item_container

    form = checkoutForm()

    print(items)
    params['items'] = items
    params['form'] = form
    return templater.render_to_response(request, 'confirmation.html', params)
