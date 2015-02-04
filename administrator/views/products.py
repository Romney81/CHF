from django import forms
from django.forms import fields, util
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
import homepage.models as hmod

templater = get_renderer('administrator')

@view_function
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
     
  
    productform = EditProductForm(initial={
        'name': product.name,
        'description': product.description,
        'category': product.category,
        'current_price': product.current_price,

    })
    
    if request.method == 'POST':
        form = EditProductForm(request.POST)
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.category = form.cleaned_data['category']
            product.current_price = form.cleaned_data['current_price']
            product.save()
            return HttpResponseRedirect('/administrator/products/')
    
    params['productform'] = productform
      
    return templater.render_to_response(request, 'products.edit.html', params)
  
class EditProductForm(forms.Form):
    name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    category = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    current_price = forms.DecimalField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    