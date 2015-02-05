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
      
    #grab all items
    params['events'] = hmod.PublicEvent.objects.all()
  

    return templater.render_to_response(request, 'events.html', params)
    
    
############################ Edit The Items  ############################# 
@view_function
def edit(request):
    params = {}
    
    try:
        event = hmod.PublicEvent.objects.get(id=request.urlparams[0])
    except:
        HttpResponseRedirect('/administrator/events/')
        
    eventform = EventEditForm(initial = {
        'name': event.name,
        'description': event.description,
        'start_date': event.start_date,
        'end_date': event.end_date,
    })
    
    if request.method =='POST':
        form = EventEditForm(request.POST)
        if form.is_valid():
            event.name = form.cleaned_data['name']
            event.description = form.cleaned_data['description']
            event.start_date = form.cleaned_data['start_date']
            event.end_date = form.cleaned_data['end_date']
            event.save()
            return HttpResponseRedirect('/administrator/events/')
            
    params['eventform'] = eventform
    
    return templater.render_to_response(request, 'events.edit.html', params)
    
class EventEditForm(forms.Form):
    name = forms.CharField(required=True, max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    start_date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}))
    end_date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}))