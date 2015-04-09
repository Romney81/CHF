from django.conf import settings
import django.contrib.auth
from django.contrib.auth import logout
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
import homepage.models as hmod

templater = get_renderer('homepage')

@view_function
def process_request(request):

    #empty params
    params = {}

    #get all events
    events = hmod.Event.objects.all()

    #month and day lists
    month = []
    day = []

    #for loop to get month and day
    for event in events:
        newmonth = event.start_date.strftime('%b')
        newday = event.start_date.strftime('%d')
        month.append(newmonth)
        day.append(newday)

    #pass event, month and day to festivals.html
    params['months'] = month
    params['days'] = day
    params['events'] = events

    return templater.render_to_response(request, 'index.html', params)


@view_function
def loginform(request):
    #prepare the login form
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            django.contrib.auth.login(request, form.user)

            return HttpResponse('''
                <script>
                    window.location.href = window.location.href;
                </script>
            ''')


    template_vars = {
      'form': form,
    }

    return templater.render_to_response(request, 'index.loginform.html', template_vars)
