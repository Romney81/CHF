# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423273752.776824
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/administrator/templates/items.edit.html'
_template_uri = 'items.edit.html'
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
        def admincontent():
            return render_admincontent(context._locals(__M_locals))
        itemform = context.get('itemform', UNDEFINED)
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
        def admincontent():
            return render_admincontent(context)
        itemform = context.get('itemform', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<div class="container">\n    <div class="manager-edit">\n        <form class="form-horizontal" method="POST">\n            ')
        __M_writer(str( itemform.non_field_errors() ))
        __M_writer('\n')
        for field in itemform:
            __M_writer('            <div class="form-group">\n                <label class="col-md-2 control-label">')
            __M_writer(str(field.label))
            __M_writer('</label>\n                <div class="col-md-10">\n                    ')
            __M_writer(str(field))
            __M_writer('\n                    <div>')
            __M_writer(str(field.errors))
            __M_writer('</div>\n                </div>\n            </div>\n')
        __M_writer('            <div class="form-group col-md-12">\n                <button type="submit" class="btn btn-lg btn-primary">Save</button>\n            </div>\n        </form>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/scottromney/SiteOne/administrator/templates/items.edit.html", "line_map": {"64": 17, "35": 1, "70": 64, "40": 23, "46": 3, "59": 10, "53": 3, "54": 7, "55": 7, "56": 8, "57": 9, "58": 10, "27": 0, "60": 12, "61": 12, "62": 13, "63": 13}, "uri": "items.edit.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
