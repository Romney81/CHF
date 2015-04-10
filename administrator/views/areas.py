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
@login_required(login_url='/homepage/user-login/')
@permission_required('admin.delete_logentry', login_url='/homepage/user-login/')
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


    form = EditAreaForm(initial={
        'name': area.name,
        'description': area.description,

    })

    if request.method == 'POST':
        form = EditAreaForm(request.POST)
        form.areaid = area.id
        if form.is_valid():
            area.name = form.cleaned_data['name']
            area.description = form.cleaned_data['description']
            area.save()
            return HttpResponseRedirect('/administrator/areas/')

    params['form'] = form

    return templater.render_to_response(request, 'areas.edit.html', params)

class EditAreaForm(forms.Form):
    name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(required=True, max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_name(self):
        event_area = hmod.Area.objects.filter(name=self.cleaned_data['name']).exclude(id=self.areaid).count()
        if event_area >= 1:
            raise forms.ValidationError("That area already exists.")

        return self.cleaned_data['name']

@view_function
def create(request):
    params = {}

    area = hmod.Area()
    area.name = ''
    area.description = ''

    area.save()

    return HttpResponseRedirect('/administrator/areas.edit/{}/'.format(area.id))

@view_function
def delete(request):
    area = hmod.Area.objects.get(id=request.urlparams[0])
    area.delete()

    return HttpResponseRedirect('/administrator/areas/')
