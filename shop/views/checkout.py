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
import requests
from django.core.mail import send_mail, EmailMessage
from django.core.validators import validate_email
import datetime

templater = get_renderer('shop')

# get total function that returns the total in the cart
def gettotal(request):

    total = 0
    if 'shopping_cart' in request.session:
        item_ids = request.session['shopping_cart']
        for key,value in item_ids.items():

            item = hmod.Item.objects.get(id = key)
            qty = value
            amount = int(item.value)

            total += (amount * qty)


        # for shopping_id in shopping_ids:
        #     shopitem = hmod.Item.objects.get(id = shopping_id)
        #     value = shopitem.value
        #
        #     total += value

    if 'rental_cart' in request.session:
        rental_ids = request.session['rental_cart']

        for rental_id in rental_ids:
            rentitem = hmod.Product.objects.get(id = rental_id)
            rentvalue = int(rentitem.current_price * 30)

            total += rentvalue

    return total


######################## main view function ########################
@view_function
@login_required(login_url='/homepage/login/')
def process_request(request):

    print('Total:', gettotal(request))
    params = {}
    API_KEY = 'd59758c3336b8c911397413a4acb1c0e'

    item_ids = request.session['shopping_cart']

    items = {}

    for key,value in item_ids.items():

        item = hmod.Item.objects.get(id = key)

        item_container = []
        item_container.append(item)
        item_container.append(value)

        items[item.id] = item_container

    form = checkoutForm()
    if request.method == 'POST':
        form = checkoutForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['expyear'])
            request.session['chargedict'] = {
                'apiKey': API_KEY,
                'currency': 'usd',
                'amount': gettotal(request),
                'type': 'Visa',
                'number': form.cleaned_data['cardnumber'],
                'exp_month': form.cleaned_data['expmonth'],
                'exp_year': form.cleaned_data['expyear'],
                'cvc': form.cleaned_data['cvc'],
                'name': form.cleaned_data['ccname'],
                'description': 'Charge for '+ request.user.email,
            }

            return HttpResponseRedirect('/shop/checkout.charge/')


    print(items)
    params['items'] = items
    params['form'] = form
    return templater.render_to_response(request, 'checkout.html', params)


class checkoutForm(forms.Form):
    YEAR_CHOICES = (('15', '15',),('2', '16',),('3', '17',),('4','18',),('5','19',),('6','20',))
    MONTH_CHOICES = (('1', '01',),('2', '02',),('3', '03',),('4','04',),('5','05',),('6','06',),('7', '07',),('8', '08',),('9', '09',),('10','10',),('11','11',),('12','12',))

    name = forms.CharField(required=True, label='Full Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))
    phone = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primary Phone'}))
    address = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Address'}))
    country = forms.ChoiceField(widget = forms.Select(attrs={'class': 'form-control'}), choices=([('1','United States'), ('2','Canada'),('3','Mexico'), ]))
    state = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}))
    city = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}))
    ccname = forms.CharField(required=True, initial='Cosmo Limesandal', label='Full Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name On Card'}))
    cardnumber = forms.CharField(required=True, initial='4732817300654', label='Card Number', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1234123412341234'}))
    expmonth = forms.ChoiceField(required=True, label='Month', initial='10', widget = forms.Select(attrs={'class': 'form-control'}), choices=MONTH_CHOICES)
    expyear = forms.ChoiceField(required=True, label='Year', initial='15', widget = forms.Select(attrs={'class': 'form-control'}), choices=YEAR_CHOICES)
    cvc = forms.CharField(required=True, label='CVC', initial='411', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '555'}))



@view_function
def charge(request):
    #API information
    API_URL = 'http://dithers.cs.byu.edu/iscore/api/v1/charges'
    params = {}
    r = requests.post(API_URL, data=request.session['chargedict'])

    #print response text
    print(r.text)

    #parse response to a dictionary
    resp = r.json()
    if 'error' in resp: #error?
        print("ERROR", resp['error'])



    else:
        print(resp.keys())
        print(resp['ID'])

        #get json data
        request.session['response'] = resp
        params['response'] = resp

        #allow all purchasable items to be returned
        if 'shopping_cart' in request.session:
            item_ids = request.session['shopping_cart']
            items = {}
            for key,value in item_ids.items():

                item = hmod.Item.objects.get(id = key)

                item_container = []
                item_container.append(item)
                item_container.append(value)
                items[item.id] = item_container

                #Create Purchase
                purch = hmod.Purchases()

                purch.custome = request.user
                purch.total = gettotal(request)
                purch.purchase_date = datetime.date.today()
                purch.charge_id = resp['ID']

                #Save new Purchase
                print(purch)

        #Purchased Items
        params['items'] = items


        #allow all rentals to be shown
        if 'rental_cart' in request.session:
            rental_ids = request.session['rental_cart']
            rentals = []
            for rental_id in rental_ids:
                rentitem = hmod.Product.objects.get(id = rental_id)
                rentals.append(rentitem)

                #create new rental
                rental = hmod.Rentals()

                rental.name = rentitem.name
                rental.rental_date = datetime.date.today()
                rental.due_date = (datetime.date.today() + datetime.timedelta(days=30))
                rental.person = request.user

                rental.save()

        #Rented Items
        params['rentals'] = rentals

        #send email
        message = templater.render(request, 'email_confirmation.html', params)
        subject = 'CHF Order Receipt'
        to = ['romney81@gmail.com']
        from_email = 'romney81@gmail.com'
        msg = EmailMessage(subject, message, to=to, from_email=from_email)
        msg.content_subtype = 'html'
        msg.send()





        return HttpResponseRedirect('/shop/checkout.confirmation/')





@view_function
def confirmation(request):
    params = {}

    #allow all purchasable items to be returned
    if 'shopping_cart' in request.session:
        item_ids = request.session['shopping_cart']
        items = {}
        for key,value in item_ids.items():

            item = hmod.Item.objects.get(id = key)

            item_container = []
            item_container.append(item)
            item_container.append(value)

            items[item.id] = item_container

    params['items'] = items


    #allow all rentals to be shown
    if 'rental_cart' in request.session:
        rental_ids = request.session['rental_cart']
        rentals = []
        for rental_id in rental_ids:
            rentitem = hmod.Product.objects.get(id = rental_id)
            rentals.append(rentitem)

    params['rentals'] = rentals

    #return json response into the view
    params['response'] = request.session['response']

    del request.session['shopping_cart']
    del request.session['rental_cart']

    #return values to the view
    return templater.render_to_response(request, 'confirmation.html', params)
