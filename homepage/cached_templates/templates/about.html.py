# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422930391.380709
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/homepage/templates/about.html'
_template_uri = 'about.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['about']


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
        def about():
            return render_about(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'about'):
            context['self'].about(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_about(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def about():
            return render_about(context)
        __M_writer = context.writer()
        __M_writer('\n\t<div class="about">\n\t\t<div class="row">\n\t\t\t<div class="col-lg-12 col-md-12 col-xs-12 col-sm-12">\n\t\t\tAbout Page\n\t\t</div>\n\t</div>\n\t\t\n\t</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/scottromney/SiteOne/homepage/templates/about.html", "line_map": {"56": 50, "34": 1, "27": 0, "44": 3, "50": 3}, "uri": "about.html"}
__M_END_METADATA
"""
