# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422672089.835227
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'footlinks', 'headlinks']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        user = context.get('user', UNDEFINED)
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def footlinks():
            return render_footlinks(context._locals(__M_locals))
        def headlinks():
            return render_headlinks(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n<!DOCTYPE html>\n<html>\n  \t<meta charset="UTF-8">\n  \t<head>\n    \t<title>Colonial Heritage Foundation</title>\n\t\t\n')
        __M_writer('\t\t<script src="//code.jquery.com/jquery-1.11.2.min.js"></script>\n\t\t<script src="//code.jquery.com/jquery-migrate-1.2.1.min.js"></script>\n\t\t<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">\n\t\t<!-- <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootswatch/3.3.1/slate/bootstrap.min.css"> -->\n\t\t<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>\n\t\t<script src="http://maps.google.com/maps/api/js?sensor=false"></script>\n\t    \n\t    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'headlinks'):
            context['self'].headlinks(**pageargs)
        

        __M_writer('\n\t\t\n\t\t<!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->\n\t    <!-- WARNING: Respond.js doesn\'t work if you view the page via file:// -->\n\t    <!--[if lt IE 9]>\n\t        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>\n\t        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>\n\t    <![endif]--> \n\t\t\n')
        __M_writer('\t\t')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\t\t\n\t\t<link rel="icon" type="image/x-icon" href="')
        __M_writer(str(STATIC_URL))
        __M_writer('/homepage/media/colonialHouse.ico" />\n  \n\t</head>\n\t<body>\n\t\t<div class="header">\n\t\t\t<div class="navbar navbar-default navbar-static-top" role="navigation">\n\t\t\t\t<div class="container">\n\t\t\t\t\t<div class="navbar-header">\n\t\t\t\t\t\t<button type="button" class="navbar-toggle" data-toggle="offcanvas" data-target="collapse">\n\t\t\t\t\t\t\t<span class="icon-bar"></span>\n\t\t\t\t\t\t\t<span class="icon-bar"></span>\n\t\t\t\t\t\t\t<span class="icon-bar"></span>\n\t\t\t\t\t\t</button>\n\t\t\t\t\t\t<a class="navbar-brand" href="/index/"><img class="nav-logo" src="')
        __M_writer(str(STATIC_URL))
        __M_writer('/homepage/media/images/logo.svg" /></a>\n\t\t\t\t\t</div>\n\t\t\t\t\t<div id="navbar" class="navbar-collapse collapse">\n\t\t\t\t\t\t<ul class="nav navbar-nav mighthide">\n\t\t\t\t\t\t\t<li><a href="/index/">Home</a></li>\n\t\t\t\t\t\t\t<li><a href="/about/">About</a></li>\n\t\t\t\t\t\t\t<li><a href="/contact/">Contact</a></li>\n\t\t\t\t\t\t\t<li><a href="/terms/">Terms</a></li>\n\t\t\t\t\t\t\t<li><a href="/shop/">Shop</a></li>\n\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t<ul class="nav navbar-nav navbar-right">\n')
        if user.is_authenticated():
            __M_writer('\t\t\t\t\t\t\t<li class="dropdown">\n\t\t\t\t\t\t\t\t<a class="dropdown-toggle" data-toggle="dropdown" href="#">\n\t\t\t\t\t\t\t\t\t')
            __M_writer(str(user.get_full_name()))
            __M_writer(' <i class="fa fa-user fa-fw"></i>  <i class="fa fa-caret-down"></i>\n\t\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t<ul class="dropdown-menu dropdown-user">\n\t\t\t\t\t\t\t\t\t<li><a href="/manager/"><i class="fa fa-user fa-fw"></i> ')
            __M_writer(str(user.get_full_name()))
            __M_writer('</a>\n\t\t\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t\t<li><a href="#"><i class="fa fa-gear fa-fw"></i> Settings</a>\n\t\t\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t\t<li class="divider"></li>\n\t\t\t\t\t\t\t\t\t<li><a href="/logout/"><i class="fa fa-sign-out fa-fw"></i> Logout</a>\n\t\t\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t\t<!-- /.dropdown-user -->\n\t\t\t\t\t\t\t</li>\n')
        else:
            __M_writer('\t\t\t\t\t\t\t<li><a href="/login/">Login</a></li>\n')
        __M_writer('\t\t\t\t\t\t</ul>\n\t\t\t\t\t</div>\t\t\t\t\t\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t</div>\n\t\t<div id="homepage" class="container">\n\t\t\t<!-- main area -->\n\t\t\t<div class="col-xs-12 col-sm-12 main-content">\n\t\t\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('     \n\t\t\t</div><!-- /.col-xs-12 main -->\n\t\t</div><!--/.container-->\n\t\t<footer class="footer">\n\t\t\t<div class="row">\n\t\t\t\t<div class="col-md-4 col-md-offset-4 beta-signup">\n\t\t\t\t\t<ul class="ccopyright">\n\t\t\t\t\t\t<li>All rights reserved.</li>\n\t\t\t\t\t\t<li><i class="fa fa-rebel"></i></li>\n\t\t\t\t\t\t<li>Design: Scott Romney</li>\n\t\t\t\t\t</ul>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t</footer>  \n')
        __M_writer('\t\t')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footlinks'):
            context['self'].footlinks(**pageargs)
        

        __M_writer('\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n           \n\t\t\t\t')
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
        __M_writer('\n\t    \n\t    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "base.htm", "line_map": {"66": 86, "67": 101, "68": 101, "69": 101, "80": 84, "74": 104, "98": 102, "16": 4, "18": 0, "110": 20, "86": 84, "92": 102, "104": 20, "33": 2, "34": 4, "35": 5, "116": 110, "39": 5, "40": 13, "45": 22, "46": 32, "47": 32, "48": 32, "49": 33, "50": 33, "51": 46, "52": 46, "53": 57, "54": 58, "55": 60, "56": 60, "57": 63, "58": 63, "59": 73, "60": 74, "61": 76}, "source_encoding": "ascii", "filename": "/Users/scottromney/SiteOne/homepage/templates/base.htm"}
__M_END_METADATA
"""
