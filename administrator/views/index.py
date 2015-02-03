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
  
    #grab all users
    params['users'] = hmod.SiteUser.objects.all()
    params['countusers'] = hmod.SiteUser.objects.count()
  
    #grab all products
    params['products'] = hmod.Product.objects.all()
    params['countproducts'] = hmod.Product.objects.count()
  
    #grab all items
    params['items'] = hmod.Item.objects.all()
    params['countitems'] = hmod.Item.objects.count()
  

    return templater.render_to_response(request, 'index.html', params)
  
  
  
############################ Edit The Users  ############################# 
@view_function
def edituser(request):
    params = {}
  
    try:
        user = hmod.SiteUser.objects.get(id=request.urlparams[0])
    except:
        HttpResponseRedirect('/administrator/index/')
     
  
    userform = UserEditForm(initial={
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'address': user.address,
        'city': user.city,
        'state': user.state,
        'zip_code': user.zip_code,
        'phone': user.phone,
    })
    
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.address = form.cleaned_data['address']
            user.city = form.cleaned_data['city']
            user.state = form.cleaned_data['state']
            user.zip_code = form.cleaned_data['zip_code']
            user.phone = form.cleaned_data['phone']
            user.save()
            return HttpResponseRedirect('/administrator/index/')
    
    params['userform'] = userform
      
    return templater.render_to_response(request, 'manager.edituser.html', params)
  
class UserEditForm(forms.Form):
    first_name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    zip_code = forms.IntegerField(required=False, min_value=0, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    
    
    
############################ Edit The Items  ############################# 
@view_function
def edititem(request):
    params = {}
  
    try:
        item = hmod.Item.objects.get(id=request.urlparams[0])
    except:
        HttpResponseRedirect('/administrator/index/')
     
  
    itemform = ItemEditForm(initial={
        'name': item.name,
        'description': item.description,
        'value': item.value,
        'is_rentable': item.is_rentable,

    })
    
    if request.method == 'POST':
        form = ItemEditForm(request.POST)
        if form.is_valid():
            item.name = form.cleaned_data['name']
            item.description = form.cleaned_data['description']
            item.value = form.cleaned_data['value']
            item.is_rentable = form.cleaned_data['is_rentable']
            item.save()
            return HttpResponseRedirect('/homepage/manager/')
    
    params['itemform'] = itemform
      
    return templater.render_to_response(request, 'manager.edititem.html', params)
  
class ItemEditForm(forms.Form):
    name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    value = forms.DecimalField(required=True, min_value=0, widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_rentable = forms.BooleanField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    