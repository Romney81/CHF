# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1421904222.004164
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/homepage/templates/userinfo.html'
_template_uri = 'userinfo.html'
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
        __M_writer('\n\t<div class="userinfo">\n\t\t<h3>Please Enter Your Information</h3>\t\t\n\t\t<div class="row">\n\t\t\t<form role="form">\n        \t\t<div class="col-xs-6 col-sm-6 col-md-6 info-column">\n\t\t\t\t\t<label for="inputUsernameEmail">First Name</label>\n\t\t\t\t\t<input type="text" class="form-control" id="inputUsernameEmail">\n\t\t\t\t\t<label for="inputUsernameEmail">Last Name</label>\n\t\t\t\t\t<input type="text" class="form-control" id="inputUsernameEmail">\n\t\t\t\t\t<label for="inputUsernameEmail">Address</label>\n\t\t\t\t\t<input type="text" class="form-control" id="inputUsernameEmail">\n\t\t\t\t\t<label for="inputUsernameEmail">City</label>\n\t\t\t\t\t<input type="text" class="form-control" id="inputUsernameEmail">\n\t\t\t\t\t<label for="inputUsernameEmail">State</label>\n\t\t\t\t\t<input type="text" class="form-control" id="inputUsernameEmail">\n\t\t\t\t</div>\n\t\t\t\t<div class="col-xs-6 col-sm-6 col-md-6 info-column">\n\t\t\t\t\t<label for="inputUsernameEmail">Zip</label>\n\t\t\t\t\t<input type="text" class="form-control" id="inputUsernameEmail">\n\t\t\t\t\t<label for="inputUsernameEmail">Country</label>\n\t\t\t\t\t<input type="text" class="form-control" id="inputUsernameEmail">\n\t\t\t\t\t<label for="inputUsernameEmail">Security Question</label>\n\t\t\t\t\t<input type="text" class="form-control" id="inputUsernameEmail">\n\t\t\t\t\t<label for="inputUsernameEmail">Answer</label>\n\t\t\t\t\t<input type="text" class="form-control" id="inputUsernameEmail">\n\t\t\t\t\t<label for="inputUsernameEmail">Phone</label>\n\t\t\t\t\t<input type="text" class="form-control" id="inputUsernameEmail">\t\t\t\t\n\t\t\t\t</div>\n\t\t\t\t<button type="submit" class="btn btn-primary finish">Finish</button>\n\t\t\t</form>\n\t\t</div>\n\t</div> \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/scottromney/SiteOne/homepage/templates/userinfo.html", "source_encoding": "ascii", "line_map": {"56": 50, "34": 1, "27": 0, "44": 3, "50": 3}, "uri": "userinfo.html"}
__M_END_METADATA
"""
