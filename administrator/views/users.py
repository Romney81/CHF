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

    return templater.render_to_response(request, 'users.html', params)
    
@view_function
def edit(request):
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
            return HttpResponseRedirect('/administrator/users/')
    
    params['userform'] = userform
      
    return templater.render_to_response(request, 'users.edit.html', params)
  
class UserEditForm(forms.Form):
    first_name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    zip_code = forms.IntegerField(required=False, min_value=0, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))