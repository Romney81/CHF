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
    