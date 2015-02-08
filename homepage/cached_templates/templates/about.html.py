# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423364927.319544
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/homepage/templates/about.html'
_template_uri = 'about.html'
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
        def index():
            return render_index(context)
        __M_writer = context.writer()
        __M_writer('\n\t<div class="about">\n\t\t<div class="row">\n\t\t\t<div class="col-md-12">\n\t\t\t\t<h2>Coming Soon!</h2>\n\t\t\t</div>\n\t\t</div>\n\t</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/scottromney/SiteOne/homepage/templates/about.html", "line_map": {"34": 1, "51": 3, "39": 11, "57": 51, "27": 0, "45": 3}, "uri": "about.html"}
__M_END_METADATA
"""
