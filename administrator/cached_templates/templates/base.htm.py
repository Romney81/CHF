# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423122151.369782
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/administrator/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['headlinks', 'administrator', 'footlinks', 'content']


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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def administrator():
            return render_administrator(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def footlinks():
            return render_footlinks(context._locals(__M_locals))
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
        __M_writer('homepage/media/thirdparties/metisMenu/dist/metisMenu.min.css" rel="stylesheet">\t\n\t<!-- Custom Fonts -->\n\t<link href="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/thirdparties/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">\t\n\t<!-- DataTables CSS -->\n    <link href="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/thirdparties/datatables-plugins/integration/bootstrap/3/dataTables.bootstrap.css" rel="stylesheet">    \n    <!-- DataTables Responsive CSS -->\n    <link href="https://cdn.datatables.net/responsive/1.0.3/css/dataTables.responsive.css" rel="stylesheet">\t\n\t<!-- Timeline CSS -->\n\t<link href="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/thirdparties/css/timeline.css" rel="stylesheet"> \t\n\t<!-- Morris Charts CSS -->\n\t<link href="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/thirdparties/morrisjs/morris.css" rel="stylesheet">\t    \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_administrator(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def administrator():
            return render_administrator(context)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footlinks(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def footlinks():
            return render_footlinks(context)
        __M_writer = context.writer()
        __M_writer('\n    <!-- DataTables JavaScript -->\n    <script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/thirdparties/DataTables/media/js/jquery.dataTables.min.js"></script>\n    <script src="https://cdn.datatables.net/responsive/1.0.3/js/dataTables.responsive.js"></script>\n    <script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/thirdparties/datatables-plugins/integration/bootstrap/3/dataTables.bootstrap.min.js"></script>\n    <script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/thirdparties/metisMenu/dist/metisMenu.min.js"></script>\n    <script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/thirdparties/raphael/raphael-min.js"></script>\n    <script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/thirdparties/morrisjs/morris.min.js"></script>\t    \n    <script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/thirdparties/js/morris-data.js"></script> \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\t\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/scottromney/SiteOne/administrator/templates/base.htm", "uri": "base.htm", "source_encoding": "ascii", "line_map": {"128": 20, "115": 30, "68": 4, "69": 6, "70": 6, "71": 8, "72": 8, "73": 10, "74": 10, "75": 14, "76": 14, "77": 16, "78": 16, "84": 19, "46": 17, "27": 0, "92": 19, "97": 22, "134": 20, "103": 25, "41": 1, "110": 25, "111": 27, "112": 27, "113": 29, "114": 29, "51": 23, "116": 30, "117": 31, "118": 31, "119": 32, "120": 32, "121": 33, "122": 33, "140": 134, "61": 4}}
__M_END_METADATA
"""
