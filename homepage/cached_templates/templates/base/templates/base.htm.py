# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428204011.812629
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/base/templates/base.htm'
_template_uri = '/base/templates/base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['shop', 'headlinks', 'administrator', 'footlinks', 'account', 'homepage']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        def headlinks():
            return render_headlinks(context._locals(__M_locals))
        def administrator():
            return render_administrator(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def homepage():
            return render_homepage(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def shop():
            return render_shop(context._locals(__M_locals))
        def footlinks():
            return render_footlinks(context._locals(__M_locals))
        def account():
            return render_account(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n<!DOCTYPE html>\n<html>\n  \t<meta charset="UTF-8">\n  \t<head>\n    \t<title>Colonial Heritage Foundation</title>\n\n')
        __M_writer('\t\t<script src="//code.jquery.com/jquery-1.11.2.min.js"></script>\n\t\t<script src="//code.jquery.com/jquery-migrate-1.2.1.min.js"></script>\n\t\t<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">\n        <link href="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/thirdparties/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">\n        <link href="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/animate.css" rel="stylesheet" type="text/css">\n\t\t<!-- <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootswatch/3.3.1/slate/bootstrap.min.css"> -->\n\t\t<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>\n        <script src="')
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


"""
__M_BEGIN_METADATA
{"uri": "/base/templates/base.htm", "filename": "/Users/scottromney/SiteOne/base/templates/base.htm", "source_encoding": "ascii", "line_map": {"115": 24, "68": 44, "133": 61, "73": 48, "139": 61, "78": 52, "109": 24, "16": 4, "145": 54, "18": 0, "83": 56, "84": 59, "85": 59, "86": 59, "151": 54, "127": 46, "91": 63, "157": 42, "97": 50, "163": 42, "38": 2, "39": 4, "40": 5, "169": 163, "103": 50, "44": 5, "45": 13, "46": 16, "47": 16, "48": 17, "49": 17, "50": 20, "51": 20, "52": 21, "53": 21, "121": 46, "58": 26, "59": 36, "60": 36, "61": 36, "62": 37, "63": 37}}
__M_END_METADATA
"""
