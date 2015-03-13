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
import datetime

templater = get_renderer('administrator')

@view_function
@login_required(login_url='/homepage/login/')
@permission_required('admin.delete_logentry', login_url='/homepage/login/')
def process_request(request):
    params = {}

    #Get todays date
    today = datetime.date.today()

    start_date = datetime.date(today.year-20, today.month, today.day)
    end_date = datetime.date(today.year, today.month, today.day-1)

    overdueitems = hmod.Rentals.objects.filter(due_date__range = (start_date, end_date))

    params['items'] = overdueitems

    return templater.render_to_response(request, 'overdue.html', params)
