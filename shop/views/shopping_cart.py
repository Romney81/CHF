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
    if 'shopping_cart' not in request.session:
        request.session['shopping_cart'] = {}
    if 'rental_cart' not in request.session:
        request.session['rental_cart'] = []

    item_ids = request.session['shopping_cart']

    items = {}


    for key,value in item_ids.items():

        item = hmod.Item.objects.get(id = key)

        item_container = []
        item_container.append(item)
        item_container.append(value)

        items[item.id] = item_container


    rent_ids = request.session['rental_cart']
    print(rent_ids)

    rentals = []

    for rents in rent_ids:

        rentalitem = hmod.Product.objects.get(id=rents)

        rentals.append(rentalitem)

    params['items'] = items
    params['rentals'] = rentals
    print(params)


    return templater.render_to_response(request, 'shopping_cart.html', params)


@view_function
def add(request):

    if 'shopping_cart' not in request.session:
        request.session['shopping_cart'] = {}

    pid = request.urlparams[0]
    qty = int(request.urlparams[1])
    rent = request.urlparams[2]

    print(rent)

    if rent == "False":
        if pid in request.session['shopping_cart']:
            request.session['shopping_cart'][pid] += qty



        else:
            request.session['shopping_cart'][pid] = qty

    else:
        if 'rental_cart' not in request.session:
            request.session['rental_cart'] = []

        if pid not in request.session['rental_cart']:
            request.session['rental_cart'].append(pid)


    request.session.modified = True
    return HttpResponseRedirect('/shop/shopping_cart/')

@view_function
def delete(request):

    pid = request.urlparams[0]

    del request.session['shopping_cart'][pid]
    request.session.modified = True




    return HttpResponseRedirect('/shop/shopping_cart/')
