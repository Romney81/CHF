# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425512280.684215
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/shop/templates/index.loginform.html'
_template_uri = 'index.loginform.html'
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
    return runtime._inherit_from(context, 'base_ajax.htm', _template_uri)
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
        

        __M_writer('\n')
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
        __M_writer('\n<div class="modal-container">\n        <div class="text-center">\n\t        <h3>Log In</h3>\n        </div>\n\n    \t<form id="loginform" autocomplete="off" class="form-horizontal signin-form" method="POST" action="/shop/index.loginform/">\n')
        if form.non_field_errors():
            __M_writer('            <div class="alert alert-danger" role="alert">\n                <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n                ')
            __M_writer(str( form.non_field_errors() ))
            __M_writer('\n            </div>\n')
        for field in form:
            __M_writer('    \t\t<div class="form-group">\n    \t\t\t<!-- <label class="col-md-3 control-label">')
            __M_writer(str(field.label))
            __M_writer('</label> -->\n    \t\t\t<div class="col-md-12">\n    \t\t\t\t')
            __M_writer(str(field))
            __M_writer('\n    \t\t\t</div>\n    \t\t</div>\n')
        __M_writer('    \t\t<button type="submit" class="btn custom">Sign In</button>\n    \t</form>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/scottromney/SiteOne/shop/templates/index.loginform.html", "uri": "index.loginform.html", "line_map": {"64": 24, "35": 1, "70": 64, "40": 27, "46": 3, "59": 17, "53": 3, "54": 10, "55": 11, "56": 13, "57": 13, "58": 16, "27": 0, "60": 18, "61": 18, "62": 20, "63": 20}, "source_encoding": "ascii"}
__M_END_METADATA
"""
