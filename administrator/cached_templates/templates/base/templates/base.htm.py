# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425363156.25717
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/base/templates/base.htm'
_template_uri = '/base/templates/base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['footlinks', 'headlinks', 'homepage', 'administrator']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        def footlinks():
            return render_footlinks(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def homepage():
            return render_homepage(context._locals(__M_locals))
        def headlinks():
            return render_headlinks(context._locals(__M_locals))
        def administrator():
            return render_administrator(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n<!DOCTYPE html>\n<html>\n  \t<meta charset="UTF-8">\n  \t<head>\n    \t<title>Colonial Heritage Foundation</title>\n\n')
        __M_writer('\t\t<script src="//code.jquery.com/jquery-1.11.2.min.js"></script>\n\t\t<script src="//code.jquery.com/jquery-migrate-1.2.1.min.js"></script>\n\t\t<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">\n\t\t<!-- <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootswatch/3.3.1/slate/bootstrap.min.css"> -->\n\t\t<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>\n        <script src="{STATIC_URL}homepage/media/thirdparties/jquery.form.js"></script>\n\t\t<script src="http://maps.google.com/maps/api/js?sensor=false"></script>\n\n\t    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'headlinks'):
            context['self'].headlinks(**pageargs)
        

        __M_writer('\n\t\t\n\t\t<!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->\n\t    <!-- WARNING: Respond.js doesn\'t work if you view the page via file:// -->\n\t    <!--[if lt IE 9]>\n\t        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>\n\t        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>\n\t    <![endif]-->\n\n')
        __M_writer('\t\t')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n\t\t<link rel="icon" type="image/x-icon" href="')
        __M_writer(str(STATIC_URL))
        __M_writer('/homepage/media/colonialHouse.ico" />\n\n\t</head>\n\t<body>\n\n    \t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'homepage'):
            context['self'].homepage(**pageargs)
        

        __M_writer('\n\n\t    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'administrator'):
            context['self'].administrator(**pageargs)
        

        __M_writer('\n\n')
        __M_writer('        ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footlinks'):
            context['self'].footlinks(**pageargs)
        

        __M_writer('\n\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footlinks(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footlinks():
            return render_footlinks(context)
        __M_writer = context.writer()
        __M_writer('\n\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_headlinks(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def headlinks():
            return render_headlinks(context)
        __M_writer = context.writer()
        __M_writer('\n\n\t    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_homepage(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def homepage():
            return render_homepage(context)
        __M_writer = context.writer()
        __M_writer('\n\n\t    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_administrator(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def administrator():
            return render_administrator(context)
        __M_writer = context.writer()
        __M_writer('\n\n\t    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "/base/templates/base.htm", "line_map": {"64": 48, "69": 52, "75": 50, "16": 4, "81": 50, "18": 0, "99": 39, "87": 21, "111": 43, "93": 21, "34": 2, "35": 4, "36": 5, "40": 5, "41": 13, "46": 23, "47": 33, "48": 33, "49": 33, "50": 34, "51": 34, "117": 43, "105": 39, "56": 41, "123": 117, "61": 45, "62": 48, "63": 48}, "source_encoding": "ascii", "filename": "/Users/scottromney/SiteOne/base/templates/base.htm"}
__M_END_METADATA
"""
