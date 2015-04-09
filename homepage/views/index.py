from django.conf import settings
import django.contrib.auth
from django.contrib.auth import logout
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer

templater = get_renderer('homepage')

@view_function
def process_request(request):
  template_vars = {
  }

  return templater.render_to_response(request, 'index.html', template_vars)


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
