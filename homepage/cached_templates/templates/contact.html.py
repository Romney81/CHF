# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1421301026.569743
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/homepage/templates/contact.html'
_template_uri = 'contact.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n<div class="contact-content">\n\t<div class="col-md-6">\n            <div class="panel panel-default">\n                <form class="form-horizontal" method="post">\n                    <fieldset>\n                        <legend class="text-center header">Contact us</legend>\n                        <div class="form-group">\n                            <div class="col-md-10 col-md-offset-1">\n                                <input id="fname" name="name" type="text" placeholder="First Name" class="form-control">\n                            </div>\n                        </div>\n                        <div class="form-group">\n                            <div class="col-md-10 col-md-offset-1">\n                                <input id="lname" name="name" type="text" placeholder="Last Name" class="form-control">\n                            </div>\n                        </div>\n\n                        <div class="form-group">\n                            <div class="col-md-10 col-md-offset-1">\n                                <input id="email" name="email" type="text" placeholder="Email Address" class="form-control">\n                            </div>\n                        </div>\n\n                        <div class="form-group">\n                            <div class="col-md-10 col-md-offset-1">\n                                <input id="phone" name="phone" type="text" placeholder="Phone" class="form-control">\n                            </div>\n                        </div>\n\n                        <div class="form-group">\n                            <div class="col-md-10 col-md-offset-1">\n                                <textarea class="form-control" id="message" name="message" placeholder="Enter your massage for us here. We will get back to you within 2 business days." rows="7"></textarea>\n                            </div>\n                        </div>\n\n                        <div class="form-group">\n                            <div class="col-md-12 text-center">\n                                <button type="submit" class="btn btn-success btn-lg contact-submit">Submit</button>\n                            </div>\n                        </div>\n                    </fieldset>\n                </form>\n            </div>\n        </div>\n        <div class="col-md-6">\n            <div>\n                <div class="panel panel-default">\n                    <div class="text-center contact-header">Our Office</div>\n                    <div class="panel-body text-center">\n                        <h4>Address</h4>\n                        <div>\n                        2217 Washington Blvd<br />\n                        Washington DC<br />\n                        (888) 888-8888<br />\n                        CHF@colonial.com<br />\n                        </div>\n                        <hr />\n                        <div id="map1" class="map">\n                        </div>\n                    </div>\n                </div>\n            </div>\n        </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "contact.html", "filename": "/Users/scottromney/SiteOne/homepage/templates/contact.html", "source_encoding": "ascii", "line_map": {"56": 50, "34": 1, "27": 0, "44": 3, "50": 3}}
__M_END_METADATA
"""
