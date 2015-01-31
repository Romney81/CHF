# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422482780.672981
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/homepage/templates/signup.html'
_template_uri = 'signup.html'
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
        form = context.get('form', UNDEFINED)
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
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n<!-- \n<div class="panel panel-default">\n\t<form class="form-signin">\n        <h2 class="form-signin-heading">Please sign in</h2>\n        <p class="text-warning">Invalid Email/Password Please Try Again</p>\n        <label for="inputEmail" class="sr-only">Email address</label>\n        <input type="email" id="inputEmail" class="form-control" placeholder="Email address" required autofocus>\n        <label for="inputPassword" class="sr-only">Password</label>\n        <input type="password" id="inputPassword" class="form-control" placeholder="Password" required>\n        <div class="checkbox">\n        \t<label><input type="checkbox" value="remember-me"> Remember me</label>\n\t\t</div>\n        <button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>\n\t</form>\n</div>\n-->\n<div class="signup">\n    <div class="row">\n\t    <div class="col-md-4 col-md-offset-2 col-xs-12">\n        <div class="user-registration">\n\t\t    <h3>Create Your Account</h3>\n            <div class="login-or">\n\t\t\t    <hr class="hr-or">\n\t\t    </div>\t\t\n\t\t    <form class="signup-form" method="POST">\n    \t\t    ')
        __M_writer(str( form.non_field_errors() ))
        __M_writer('\n')
        for field in form:
            __M_writer('                    <div class="form-group">\n                        <label class="col-md-2 control-label">')
            __M_writer(str(field.label))
            __M_writer('</label>\n                        <div class="col-md-10">\n                        ')
            __M_writer(str(field))
            __M_writer(' \n                        <div class="form-constrol" style="padding-left: 0px">')
            __M_writer(str(field.errors))
            __M_writer('</div>\n\t\t\t            </div>\n\t\t            </div>\n')
        __M_writer('\t        \n    \t        <button type="submit" class="btn btn btn-primary">\n    \t          Create Account\n    \t        </button>\n\t        </form>\n\t    </div>\n\t</div>\n\t<div class="col-md-4 col-xs-12">\n\t<div class="vendor-registration">\n\t\t<h3>Register as a Vendor</h3>\n\t\t<div class="login-or">\n\t\t\t<hr class="hr-or">\n\t\t</div>\n\t\t\n\t\t<form role="form">\n\t        <div class="form-group">\n\t          \t<label for="inputUsernameEmail">Company Name</label>\n\t\t\t  \t<input type="text" class="form-control" id="inputUsernameEmail">\n\t        </div>\n\t        <div class="form-group">\n\t          \t<label for="inputPassword">Email</label>\n\t\t\t  \t<input type="text" class="form-control" id="inputPassword">\n\t        </div>\n\t        <div class="form-group">\n\t         \t <label for="inputPassword">Phone</label>\n\t\t\t \t <input type="text" class="form-control" id="inputPassword">\n\t        </div>\n\t        <button type="submit" class="btn btn btn-primary">\n\t          Register\n\t        </button>\n\t      </form>\n\t</div>\n\t</div>\n</div>\n</div>\n</div> \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"35": 1, "69": 63, "45": 3, "27": 0, "52": 3, "53": 29, "54": 29, "55": 30, "56": 31, "57": 32, "58": 32, "59": 34, "60": 34, "61": 35, "62": 35, "63": 39}, "filename": "/Users/scottromney/SiteOne/homepage/templates/signup.html", "uri": "signup.html"}
__M_END_METADATA
"""
