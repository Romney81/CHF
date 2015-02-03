# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422930456.328945
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'index', 'headlinks', 'homepage', 'footlinks', 'about', 'contact', 'login']


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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def index():
            return render_index(context._locals(__M_locals))
        def about():
            return render_about(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        def footlinks():
            return render_footlinks(context._locals(__M_locals))
        def contact():
            return render_contact(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def headlinks():
            return render_headlinks(context._locals(__M_locals))
        def homepage():
            return render_homepage(context._locals(__M_locals))
        def login():
            return render_login(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'headlinks'):
            context['self'].headlinks(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'homepage'):
            context['self'].homepage(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footlinks'):
            context['self'].footlinks(**pageargs)
        

        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n       \n    \t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_index(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def index():
            return render_index(context)
        __M_writer = context.writer()
        __M_writer('\n       \n    \t\t')
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
        __M_writer('\n    <!-- Custom Fonts -->\n\t<link href="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/thirdparties/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">\t    \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_homepage(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def index():
            return render_index(context)
        def about():
            return render_about(context)
        user = context.get('user', UNDEFINED)
        def contact():
            return render_contact(context)
        def content():
            return render_content(context)
        def homepage():
            return render_homepage(context)
        def login():
            return render_login(context)
        __M_writer = context.writer()
        __M_writer('\n    <div class="header">\n    \t<div class="navbar navbar-top navbar-fixed-top" role="navigation">\n    \t\t<div class="container">\n    \t\t\t<div class="navbar-header">\n    \t\t\t\t<button type="button" class="navbar-toggle" data-toggle="offcanvas" data-target="collapse">\n    \t\t\t\t\t<span class="icon-bar"></span>\n    \t\t\t\t\t<span class="icon-bar"></span>\n    \t\t\t\t\t<span class="icon-bar"></span>\n    \t\t\t\t</button>\n    \t\t\t\t<a class="navbar-brand" href="/index/">\n    \t\t\t\t\t<img class="nav-logo" src="')
        __M_writer(str(STATIC_URL))
        __M_writer('/homepage/media/images/logo.svg" />\n    \t\t\t\t\t<img class="nav-logo nav-logo-dark" src="')
        __M_writer(str(STATIC_URL))
        __M_writer('/homepage/media/images/logo-dark.svg" />\n    \t\t\t    </a>\n    \t\t\t</div>\n    \t\t\t<div id="navbar" class="navbar-collapse collapse">\n    \t\t\t\t<ul class="nav navbar-nav mighthide">\n    \t\t\t\t\t<li><a href="/index/">Home</a></li>\n    \t\t\t\t\t<li><a href="/about/">About</a></li>\n    \t\t\t\t\t<li><a href="/contact/">Contact</a></li>\n    \t\t\t\t\t<li><a href="/terms/">Terms</a></li>\n    \t\t\t\t\t<li><a href="/shop/">Shop</a></li>\n    \t\t\t\t</ul>\n    \t\t\t\t<ul class="nav navbar-nav navbar-right">\n')
        if user.is_authenticated():
            __M_writer('    \t\t\t\t\t<li class="dropdown">\n    \t\t\t\t\t\t<a class="dropdown-toggle" data-toggle="dropdown" href="#">\n    \t\t\t\t\t\t\t')
            __M_writer(str(user.get_full_name()))
            __M_writer(' <i class="fa fa-user fa-fw"></i>  <i class="fa fa-caret-down"></i>\n    \t\t\t\t\t\t</a>\n    \t\t\t\t\t\t<ul class="dropdown-menu dropdown-user">\n    \t\t\t\t\t\t\t<li><a href="/manager/"><i class="fa fa-user fa-fw"></i> ')
            __M_writer(str(user.get_full_name()))
            __M_writer('</a>\n    \t\t\t\t\t\t\t</li>\n    \t\t\t\t\t\t\t<li><a href="#"><i class="fa fa-gear fa-fw"></i> Settings</a>\n    \t\t\t\t\t\t\t</li>\n    \t\t\t\t\t\t\t<li class="divider"></li>\n    \t\t\t\t\t\t\t<li><a href="/logout/"><i class="fa fa-sign-out fa-fw"></i> Logout</a>\n    \t\t\t\t\t\t\t</li>\n    \t\t\t\t\t\t</ul>\n    \t\t\t\t\t<!-- /.dropdown-user -->\n    \t\t\t\t\t</li>\n')
        else:
            __M_writer('    \t\t\t\t\t<li><a href="/login/">Login</a></li>\n')
        __M_writer('    \t\t\t\t</ul>\n    \t\t\t</div>\t\t\t\t\t\n    \t\t</div>\n    \t</div>\n    </div>\n    \n    <div id="homepage" class="container">\n    \t<div class="hero col-sm-12">\n    \t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'index'):
            context['self'].index(**pageargs)
        

        __M_writer('\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'login'):
            context['self'].login(**pageargs)
        

        __M_writer('\n    \t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'about'):
            context['self'].about(**pageargs)
        

        __M_writer('\n    \t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'contact'):
            context['self'].contact(**pageargs)
        

        __M_writer('\n        </div>\n    \t<!-- main area -->\n    \t<div class="col-xs-12 col-sm-12 main-content">\n    \t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('     \n    \t</div><!-- /.col-xs-12 main -->\n    </div><!--/.container-->\n    <footer class="footer">\n    \t<div class="row">\n    \t\t<div class="col-md-4 col-md-offset-4 beta-signup">\n    \t\t\t<ul class="ccopyright">\n    \t\t\t\t<li>All rights reserved.</li>\n    \t\t\t\t<li><i class="fa fa-rebel"></i></li>\n    \t\t\t\t<li>Design: Scott Romney</li>\n    \t\t\t</ul>\n    \t\t</div>\n    \t</div>\n    </footer>  \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footlinks(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footlinks():
            return render_footlinks(context)
        __M_writer = context.writer()
        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_about(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def about():
            return render_about(context)
        __M_writer = context.writer()
        __M_writer('\n       \n    \t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_contact(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def contact():
            return render_contact(context)
        __M_writer = context.writer()
        __M_writer('\n       \n    \t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_login(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def login():
            return render_login(context)
        __M_writer = context.writer()
        __M_writer('\n       \n    \t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/scottromney/SiteOne/homepage/templates/base.htm", "line_map": {"128": 8, "65": 94, "130": 19, "131": 20, "132": 20, "133": 32, "134": 33, "71": 74, "136": 35, "129": 19, "138": 38, "139": 48, "140": 49, "77": 74, "141": 51, "208": 62, "146": 61, "83": 59, "196": 68, "214": 62, "151": 64, "137": 38, "89": 59, "27": 0, "156": 67, "95": 3, "161": 70, "166": 76, "102": 3, "103": 5, "104": 5, "220": 214, "135": 35, "172": 92, "178": 92, "110": 8, "50": 1, "55": 6, "184": 65, "60": 90, "202": 68, "190": 65}, "uri": "base.htm"}
__M_END_METADATA
"""
