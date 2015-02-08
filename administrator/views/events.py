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

    form = EventEditForm(initial = {
        'name': event.name,
        'description': event.description,
        'start_date': event.start_date,
        'end_date': event.end_date,
    })

    if request.method =='POST':
        form = EventEditForm(request.POST)
        form.eventid = event.id
        if form.is_valid():
            event.name = form.cleaned_data['name']
            event.description = form.cleaned_data['description']
            event.start_date = form.cleaned_data['start_date']
            event.end_date = form.cleaned_data['end_date']
            event.save()
            return HttpResponseRedirect('/administrator/events/')

    params['form'] = form

    return templater.render_to_response(request, 'events.edit.html', params)

class EventEditForm(forms.Form):
    name = forms.CharField(required=True, max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class': 'form-control'}))
    start_date = forms.DateField(widget=DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": False}))
    end_date = forms.DateField(widget=DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": False}))

    def clean_name(self):
        event_count = hmod.PublicEvent.objects.filter(name=self.cleaned_data['name']).exclude(id=self.eventid).count()
        if event_count >= 1:
            raise forms.ValidationError("That event already exists.")

        return self.cleaned_data['name']

@view_function
def create(request):
    params = {}

    event = hmod.PublicEvent()
    event.name = ''
    event.description = ''
    event.start_date = '1999-12-12'
    event.end_date = '1999-12-12'

    event.save()

    return HttpResponseRedirect('/administrator/events.edit/{}/'.format(event.id))

@view_function
def delete(request):
    event = hmod.PublicEvent.objects.get(id=request.urlparams[0])
    event.delete()

    return HttpResponseRedirect('/administrator/events/')
