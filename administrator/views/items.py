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
    params['items'] = hmod.Item.objects.all()


    return templater.render_to_response(request, 'items.html', params)


############################ Edit The Items  #############################
@view_function
def edit(request):
    params = {}

    try:
        item = hmod.Item.objects.get(id=request.urlparams[0])
    except:
        HttpResponseRedirect('/administrator/items/')


    form = ItemEditForm(initial={
        'name': item.name,
        'description': item.description,
        'value': item.value,
        'is_rentable': item.is_rentable,

    })
    if request.method == 'POST':
        form = ItemEditForm(request.POST)
        form.itemid = item.id
        if form.is_valid():
            item.name = form.cleaned_data['name']
            item.description = form.cleaned_data['description']
            item.value = form.cleaned_data['value']
            item.is_rentable = form.cleaned_data['is_rentable']
            item.save()
            return HttpResponseRedirect('/administrator/items/')

    params['form'] = form

    return templater.render_to_response(request, 'items.edit.html', params)

class ItemEditForm(forms.Form):
    name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    value = forms.DecimalField(required=False, min_value=0, widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_rentable = forms.BooleanField(required=False)

    def clean_name(self):
        item_count = hmod.Item.objects.filter(name=self.cleaned_data['name']).exclude(id=self.itemid).count()
        if item_count >= 1:
            raise forms.ValidationError("That item already exists.")

        return self.cleaned_data['name']

@view_function
def create(request):
    params = {}

    item = hmod.Item()
    item.name = ''
    item.description = ''
    item.value = '0.0'

    item.save()

    return HttpResponseRedirect('/administrator/items.edit/{}/'.format(item.id))

@view_function
def delete(request):
    item = hmod.Item.objects.get(id=request.urlparams[0])
    item.delete()

    return HttpResponseRedirect('/administrator/items/')
