# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423265889.464754
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/homepage/templates/signup.html'
_template_uri = 'signup.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['index']


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
        def index():
            return render_index(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'index'):
            context['self'].index(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_index(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def index():
            return render_index(context)
        __M_writer = context.writer()
        __M_writer('\n    <!--\n<div class="panel panel-default">\n\t<form class="form-signin">\n        <h2 class="form-signin-heading">Please sign in</h2>\n        <p class="text-warning">Invalid Email/Password Please Try Again</p>\n        <label for="inputEmail" class="sr-only">Email address</label>\n        <input type="email" id="inputEmail" class="form-control" placeholder="Email address" required autofocus>\n        <label for="inputPassword" class="sr-only">Password</label>\n        <input type="password" id="inputPassword" class="form-control" placeholder="Password" required>\n        <div class="checkbox">\n        \t<label><input type="checkbox" value="remember-me"> Remember me</label>\n\t\t</div>\n        <button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>\n\t</form>\n</div>\n-->\n    <div class="signup">\n        <div class="row">\n            <div class="row">\n                <div class="col-md-12">\n                    <h3>Sign Up</h3>\n                </div>\n                <form class="form-horizontal signin-form" method="POST">\n                    ')
        __M_writer(str( form.non_field_errors() ))
        __M_writer('\n')
        for field in form:
            __M_writer('                    <div class="form-group col-md-12">\n                        <!-- <label class="col-md-3 control-label">')
            __M_writer(str(field.label))
            __M_writer('</label> -->\n                        <div class="col-md-12">\n                            ')
            __M_writer(str(field))
            __M_writer('\n                        </div>\n                    </div>\n')
        __M_writer('                    <div class="form-group col-md-12">\n                        <button type="submit" class="btn btn-primary">Sign Up</button>\n                    </div>\n                </form>\n            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"35": 1, "68": 62, "40": 43, "46": 3, "59": 30, "53": 3, "54": 27, "55": 27, "56": 28, "57": 29, "58": 30, "27": 0, "60": 32, "61": 32, "62": 36}, "source_encoding": "ascii", "filename": "/Users/scottromney/SiteOne/homepage/templates/signup.html", "uri": "signup.html"}
__M_END_METADATA
"""
