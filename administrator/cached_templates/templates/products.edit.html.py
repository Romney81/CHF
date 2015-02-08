# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423371503.30189
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/administrator/templates/products.edit.html'
_template_uri = 'products.edit.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['admincontent']


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
    return runtime._inherit_from(context, 'index.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        form = context.get('form', UNDEFINED)
        def admincontent():
            return render_admincontent(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'admincontent'):
            context['self'].admincontent(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_admincontent(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def admincontent():
            return render_admincontent(context)
        __M_writer = context.writer()
        __M_writer('\n    <div class="container">\n        <div class="manager-edit">\n            <div class="row">\n                <div class="panel panel-default col-md-12 col-sm-12">\n                    <div class="panel-heading">\n                        <h3 class="panel-title">Edit Product</h3>\n                    </div>\n                    <div class="panel-body">\n                        <form class="form-horizontal signin-form" method="POST">\n                            ')
        __M_writer(str( form.non_field_errors() ))
        __M_writer('\n')
        for field in form:
            __M_writer('                            <div class="form-group">\n                                <label class="col-md-2 control-label">')
            __M_writer(str(field.label))
            __M_writer('</label>\n                                <div class="col-md-8">\n                                    ')
            __M_writer(str(field))
            __M_writer('\n                                    <p>')
            __M_writer(str(field.errors))
            __M_writer('</p>\n                                </div>\n                            </div>\n')
        __M_writer('                            <div class="col-md-offset-2 col-md-2 save-btn-col">\n                                <button type="submit" class="btn btn-lg btn-white">Save</button>\n                            </div>\n                        </form>\n                    </div>\n                </div>\n            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"64": 23, "35": 1, "70": 64, "40": 32, "46": 3, "59": 16, "53": 3, "54": 13, "55": 13, "56": 14, "57": 15, "58": 16, "27": 0, "60": 18, "61": 18, "62": 19, "63": 19}, "uri": "products.edit.html", "filename": "/Users/scottromney/SiteOne/administrator/templates/products.edit.html"}
__M_END_METADATA
"""
