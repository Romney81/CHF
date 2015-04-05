from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',


    url(r'^admin/', include(admin.site.urls)),
    # the django_mako_plus controller handles every request - this line is the glue that connects Mako to Django
    url(r'^.*$', 'django_mako_plus.controller.router.route_request' ),
)
