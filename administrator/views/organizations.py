from django import forms
from bootstrap3_datetime.widgets import DateTimePicker
from django.forms import fields, util
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
import homepage.models as hmod
import datetime

templater = get_renderer('administrator')

@view_function
def process_request(request):
    params = {}

    #grab all organizations
    params['organizations'] = hmod.Organization.objects.all()
    return templater.render_to_response(request, 'organizations.html', params)


############################ Edit The Organization  #############################
@view_function
def edit(request):
    params = {}

    try:
        organization = hmod.Organization.objects.get(id=request.urlparams[0])
    except:
        HttpResponseRedirect('/administrator/organizations/')


    organizationform = EditOrganizationForm(initial={
        'organization_type': organization.organization_type,
        'phone': organization.phone,
        'creation_date': organization.creation_date,
        'address1': organization.address1,
        'city': organization.city,
        'state': organization.state,
        'zip_code': organization.zip_code,
        'email': organization.email,
    })

    if request.method == 'POST':
        form = EditOrganizationForm(request.POST)
        if form.is_valid():
            organization.organization_type = form.cleaned_data['organization_type']
            organization.phone = form.cleaned_data['phone']
            organization.creation_date = form.cleaned_data['creation_date']
            organization.address1 = form.cleaned_data['address1']
            organization.city = form.cleaned_data['city']
            organization.state = form.cleaned_data['state']
            organization.zip_code = form.cleaned_data['zip_code']
            organization.email = form.cleaned_data['email']
            organization.save()
            return HttpResponseRedirect('/administrator/organizations/')

    params['organizationform'] = organizationform

    return templater.render_to_response(request, 'organizations.edit.html', params)

class EditOrganizationForm(forms.Form):
    organization_type = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    creation_date = forms.DateField(widget=DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": False}))
    address1 = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    zip_code = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))


@view_function
def create(request):
    params = {}

    organization = hmod.Organization()


    organization.save()

    return HttpResponseRedirect('/administrator/organizations.edit/{}/'.format(organization.id))
