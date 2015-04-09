# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428558590.541441
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/administrator/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['headlinks', 'content', 'footlinks', 'administrator']


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
    return runtime._inherit_from(context, '/base/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def headlinks():
            return render_headlinks(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def footlinks():
            return render_footlinks(context._locals(__M_locals))
        def administrator():
            return render_administrator(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'headlinks'):
            context['self'].headlinks(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'administrator'):
            context['self'].administrator(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footlinks'):
            context['self'].footlinks(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_headlinks(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def headlinks():
            return render_headlinks(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <!-- MetisMenu CSS -->\n\t<link href="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/thirdparties/metisMenu/dist/metisMenu.min.css" rel="stylesheet">\n\t<!-- Switch CSS -->\n\t<link href="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/thirdparties/switch/css/bootstrap-switch.min.css" rel="stylesheet">\n\t<!-- Custom Fonts -->\n\t<link href="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/thirdparties/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">\n\t<!-- DataTables CSS -->\n    <link href="https://cdn.datatables.net/plug-ins/1.10.6/integration/bootstrap/3/dataTables.bootstrap.css" rel="stylesheet">\n    <!-- DataTables Responsive CSS -->\n    <link href="https://cdn.datatables.net/responsive/1.0.3/css/dataTables.responsive.css" rel="stylesheet">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footlinks(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footlinks():
            return render_footlinks(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <!-- DataTables JavaScript -->\n    <script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/thirdparties/DataTables/media/js/jquery.dataTables.min.js"></script>\n    <script src="https://cdn.datatables.net/plug-ins/1.10.6/integration/bootstrap/3/dataTables.bootstrap.js"></script>\n    <script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/thirdparties/datatables-plugins/integration/bootstrap/3/dataTables.bootstrap.min.js"></script>\n    <script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/thirdparties/metisMenu/dist/metisMenu.min.js"></script>\n\t<script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/thirdparties/switch/js/bootstrap-switch.min.js"></script>\n\t<script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/thirdparties/bootstrap-notify.min.js"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_administrator(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        def administrator():
            return render_administrator(context)
        __M_writer = context.writer()
        __M_writer('\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"129": 20, "69": 4, "70": 6, "71": 6, "72": 8, "73": 8, "74": 10, "75": 10, "81": 18, "110": 30, "87": 18, "27": 0, "135": 129, "93": 23, "100": 23, "101": 25, "102": 25, "103": 27, "104": 27, "41": 1, "106": 28, "107": 29, "108": 29, "109": 30, "46": 15, "51": 21, "116": 17, "105": 28, "56": 31, "124": 17, "62": 4}, "source_encoding": "ascii", "uri": "base.htm", "filename": "/Users/scottromney/SiteOne/administrator/templates/base.htm"}
__M_END_METADATA
"""
