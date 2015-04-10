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
from datetime import timedelta
from django.core.mail import send_mail, EmailMessage
from django.core.validators import validate_email

templater = get_renderer('administrator')

@view_function
@login_required(login_url='/homepage/user-login/')
@permission_required('admin.delete_logentry', login_url='/homepage/user-login/')
def process_request(request):
    params = {}

    #Get todays date
    today = datetime.date.today()
    thirdydays = today - timedelta(days=30)
    sixtydays = today - timedelta(days=60)
    nintydays = today - timedelta(days=90)

    #get all rental objects within these dates
    overdue_thirty = hmod.Rentals.objects.filter(due_date__range=(sixtydays, thirdydays))
    overdue_sixty = hmod.Rentals.objects.filter(due_date__range=(nintydays, sixtydays))
    overdue_ninty = hmod.Rentals.objects.filter(due_date__lt=nintydays)

    #pass lists to the view
    params['thirty'] = overdue_thirty
    params['sixty'] = overdue_sixty
    params['ninety'] = overdue_ninty

    #return View
    return templater.render_to_response(request, 'overdue.html', params)

@view_function
def sendmail(request):
    params = {}
    print('############## Made It ##############')
    #Get todays date
    today = datetime.date.today()
    thirdydays = today - timedelta(days=30)
    sixtydays = today - timedelta(days=60)
    nintydays = today - timedelta(days=90)

    mail = request.urlparams[0]
    mail_list = []
    if mail == '30':
        overdue_thirty = hmod.Rentals.objects.filter(due_date__range=(sixtydays, thirdydays))
        for rental in overdue_thirty:
            email = rental.person.email
            mail_list.append(email)

    if mail == '60':
        overdue_sixty = hmod.Rentals.objects.filter(due_date__range=(nintydays, sixtydays))
        for rental in overdue_sixty:
            email = rental.person.email
            mail_list.append(email)
    if mail == '90':
        overdue_ninty = hmod.Rentals.objects.filter(due_date__lt=nintydays)
        for rental in overdue_ninty:
            email = rental.person.email
            mail_list.append(email)


    #send email
    message = templater.render(request, 'email_reminder.html', params)
    subject = 'CHF Order Receipt'
    to = mail_list
    from_email = 'romney81@gmail.com'
    msg = EmailMessage(subject, message, to=to, from_email=from_email)
    msg.content_subtype = 'html'
    msg.send()

    return HttpResponseRedirect('/administrator/overdue/')
