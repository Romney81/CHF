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
    item_count = 0

    for key,value in item_ids.items():

        item = hmod.Item.objects.get(id = key)

        item_container = []
        item_container.append(item)
        item_container.append(value)
        item_count += 1

        items[item.id] = item_container

    rental_ids = request.session['rental_cart']

    rentals = []

    for rental in rental_ids:

        rents = hmod.Product.objects.get(id = rental)

        rentals.append(rents)
        item_count += 1




    params['item_count'] = item_count
    params['items'] = items
    params['rentals'] = rentals
    return templater.render_to_response(request, 'view-cart.html', params)

@view_function
def delete(request):
    print(request.session['shopping_cart'])
    print(request.session['rental_cart'])
    pid = request.urlparams[0]
    rent = request.urlparams[1]
    print(int(pid))
    #Determines if item is rental or not
    if rent == "False":
        del request.session['shopping_cart'][pid]
    else:
        request.session['rental_cart'].remove(pid)

    #Tell django the session has been modified for reload.
    request.session.modified = True

    return HttpResponseRedirect('/shop/view-cart/')
