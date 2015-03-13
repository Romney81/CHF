# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425782244.194856
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/shop/templates/account.changepassword.html'
_template_uri = 'account.changepassword.html'
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
        def content():
            return render_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
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
        def content():
            return render_content(context)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <form id="user_changepassword" class="form-horizontal" method="POST"  action="/shop/account.changepassword/">\n        ')
        __M_writer(str(form.non_field_errors()))
        __M_writer('\n')
        for field in form:
            __M_writer('        <div class="form-group">\n            <label class="col-md-3 control-label">')
            __M_writer(str(field.label))
            __M_writer('</label>\n            <div class="col-md-8">\n                ')
            __M_writer(str(field))
            __M_writer('\n                <p>\n                    ')
            __M_writer(str(field.errors))
            __M_writer('\n                </p>\n            </div>\n        </div>\n')
        __M_writer('        <div class="text-center">\n            <button type="submit" class="btn btn-lg btn-blue">Save</button>\n        </div>\n\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/scottromney/SiteOne/shop/templates/account.changepassword.html", "uri": "account.changepassword.html", "line_map": {"64": 17, "35": 1, "70": 64, "40": 22, "46": 3, "59": 8, "53": 3, "54": 5, "55": 5, "56": 6, "57": 7, "58": 8, "27": 0, "60": 10, "61": 10, "62": 12, "63": 12}, "source_encoding": "ascii"}
__M_END_METADATA
"""
