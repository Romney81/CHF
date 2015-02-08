from django import forms
from django.forms import fields, util
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
import homepage.models as hmod

templater = get_renderer('administrator')

@view_function
@login_required(login_url='/homepage/login/')
@permission_required('admin.delete_logentry', login_url='/homepage/login/')
def process_request(request):
    params = {}

    #grab all products
    params['products'] = hmod.Product.objects.all()
    return templater.render_to_response(request, 'products.html', params)


############################ Edit The Products  #############################
@view_function
def edit(request):
    params = {}

    try:
        product = hmod.Product.objects.get(id=request.urlparams[0])
    except:
        HttpResponseRedirect('/administrator/products/')


    form = EditProductForm(initial={
        'name': product.name,
        'description': product.description,
        'category': product.category,
        'current_price': product.current_price,

    })

    if request.method == 'POST':
        form = EditProductForm(request.POST)
        form.productid = product.id
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.category = form.cleaned_data['category']
            product.current_price = form.cleaned_data['current_price']
            product.save()
            return HttpResponseRedirect('/administrator/products/')

    params['form'] = form

    return templater.render_to_response(request, 'products.edit.html', params)

class EditProductForm(forms.Form):
    name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    category = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    current_price = forms.DecimalField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_name(self):
        product_count = hmod.Product.objects.filter(name=self.cleaned_data['name']).exclude(id=self.productid).count()
        if product_count >= 1:
            raise forms.ValidationError("That product already exists.")

        return self.cleaned_data['name']
@view_function
def create(request):
    params = {}

    product = hmod.Product()
    product.name = ''
    product.category = ''
    product.current_price = '0.0'

    product.save()

    return HttpResponseRedirect('/administrator/products.edit/{}/'.format(product.id))


@view_function
def delete(request):
    product = hmod.Product.objects.get(id=request.urlparams[0])
    product.delete()

    return HttpResponseRedirect('/administrator/products/')
