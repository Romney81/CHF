# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425606052.449877
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/shop/templates/index2.html'
_template_uri = 'index2.html'
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
        items = context.get('items', UNDEFINED)
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
        items = context.get('items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        for item in items:
            __M_writer('<div class="item_container">\n    <p>\n        ')
            __M_writer(str(item.name))
            __M_writer('\n    </p>\n    <p>\n        ')
            __M_writer(str(item.description))
            __M_writer('\n    </p>\n    <p>\n        ')
            __M_writer(str(item.value))
            __M_writer('\n    </p>\n    <p class="quantity">\n        1\n    </p>\n    <button data-pid="')
            __M_writer(str(item.id))
            __M_writer('" class="btn btn-primary add_button"> Add to Cart</button>\n\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "index2.html", "filename": "/Users/scottromney/SiteOne/shop/templates/index2.html", "line_map": {"35": 1, "69": 63, "40": 23, "46": 3, "59": 11, "53": 3, "54": 5, "55": 6, "56": 8, "57": 8, "58": 11, "27": 0, "60": 14, "61": 14, "62": 19, "63": 19}}
__M_END_METADATA
"""
