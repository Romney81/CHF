from django.conf import settings
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from datetime import datetime

templater = get_renderer('homepage')

@view_function
def process_request(request):
  template_vars = {
    
  }
  return templater.render_to_response(request, 'exhibits.html', template_vars)
