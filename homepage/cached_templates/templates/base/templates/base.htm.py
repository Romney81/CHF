# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425619134.319963
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/base/templates/base.htm'
_template_uri = '/base/templates/base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['headlinks', 'shop', 'footlinks', 'homepage', 'account', 'administrator']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def headlinks():
            return render_headlinks(context._locals(__M_locals))
        def shop():
            return render_shop(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def administrator():
            return render_administrator(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def footlinks():
            return render_footlinks(context._locals(__M_locals))
        def homepage():
            return render_homepage(context._locals(__M_locals))
        def account():
            return render_account(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n<!DOCTYPE html>\n<html>\n  \t<meta charset="UTF-8">\n  \t<head>\n    \t<title>Colonial Heritage Foundation</title>\n\n')
        __M_writer('\t\t<script src="//code.jquery.com/jquery-1.11.2.min.js"></script>\n\t\t<script src="//code.jquery.com/jquery-migrate-1.2.1.min.js"></script>\n\t\t<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">\n        <link href="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/thirdparties/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">\n\t\t<!-- <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootswatch/3.3.1/slate/bootstrap.min.css"> -->\n\t\t<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>\n        <script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/thirdparties/jquery.form.js"></script>\n        <script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/thirdparties/loadmodal.js"></script>\n\t\t<!--<script src="http://maps.google.com/maps/api/js?sensor=false"></script>-->\n\n\t    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'headlinks'):
            context['self'].headlinks(**pageargs)
        

        __M_writer('\n\n\t\t<!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->\n\t    <!-- WARNING: Respond.js doesn\'t work if you view the page via file:// -->\n\t    <!--[if lt IE 9]>\n\t        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>\n\t        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>\n\t    <![endif]-->\n\n')
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
        

        __M_writer('\n\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'shop'):
            context['self'].shop(**pageargs)
        

        __M_writer('\n\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'account'):
            context['self'].account(**pageargs)
        

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


def render_shop(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def shop():
            return render_shop(context)
        __M_writer = context.writer()
        __M_writer('\n\n\t    ')
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


def render_account(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def account():
            return render_account(context)
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
{"filename": "/Users/scottromney/SiteOne/base/templates/base.htm", "source_encoding": "ascii", "uri": "/base/templates/base.htm", "line_map": {"66": 43, "131": 41, "71": 47, "167": 161, "137": 41, "76": 51, "143": 53, "16": 4, "81": 55, "18": 0, "83": 58, "84": 58, "149": 53, "89": 62, "155": 45, "125": 60, "95": 23, "161": 45, "82": 58, "101": 23, "38": 2, "39": 4, "40": 5, "107": 49, "44": 5, "45": 13, "46": 16, "47": 16, "48": 19, "49": 19, "50": 20, "51": 20, "113": 49, "119": 60, "56": 25, "57": 35, "58": 35, "59": 35, "60": 36, "61": 36}}
__M_END_METADATA
"""
