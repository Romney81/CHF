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

    #grab all Areas
    params['areas'] = hmod.Area.objects.all()
    return templater.render_to_response(request, 'areas.html', params)


############################ Edit The Areas  #############################
@view_function
def edit(request):
    params = {}

    try:
        area = hmod.Area.objects.get(id=request.urlparams[0])
    except:
        HttpResponseRedirect('/administrator/areas/')


    areaform = EditAreaForm(initial={
        'name': area.name,
        'description': area.description,

    })

    if request.method == 'POST':
        form = EditAreaForm(request.POST)
        if form.is_valid():
            area.name = form.cleaned_data['name']
            area.description = form.cleaned_data['description']
            area.save()
            return HttpResponseRedirect('/administrator/areas/')

    params['areaform'] = areaform

    return templater.render_to_response(request, 'areas.edit.html', params)

class EditAreaForm(forms.Form):
    name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(required=True, max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}))

@view_function
def create(request):
    params = {}

    area = hmod.Area()
    area.name = ''
    area.description = ''

    area.save()

    return HttpResponseRedirect('/administrator/areas.edit/{}/'.format(area.id))
