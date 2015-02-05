# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423103031.344041
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['contact', 'footlinks', 'about', 'homepage', 'headlinks', 'index', 'login', 'content']


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
        def contact():
            return render_contact(context._locals(__M_locals))
        def homepage():
            return render_homepage(context._locals(__M_locals))
        def headlinks():
            return render_headlinks(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def footlinks():
            return render_footlinks(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        def about():
            return render_about(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def index():
            return render_index(context._locals(__M_locals))
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


def render_homepage(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def contact():
            return render_contact(context)
        def homepage():
            return render_homepage(context)
        def content():
            return render_content(context)
        user = context.get('user', UNDEFINED)
        def about():
            return render_about(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def index():
            return render_index(context)
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
            __M_writer(' <i class="fa fa-user fa-fw"></i>  <i class="fa fa-caret-down"></i>\n    \t\t\t\t\t\t</a>\n    \t\t\t\t\t\t<ul class="dropdown-menu dropdown-user">\n    \t\t\t\t\t\t\t<li><a href="/administrator/"><i class="fa fa-user fa-fw"></i> ')
            __M_writer(str(user.get_full_name()))
            __M_writer('</a>\n    \t\t\t\t\t\t\t</li>\n    \t\t\t\t\t\t\t<li><a href="#"><i class="fa fa-gear fa-fw"></i> Settings</a>\n    \t\t\t\t\t\t\t</li>\n    \t\t\t\t\t\t\t<li class="divider"></li>\n    \t\t\t\t\t\t\t<li><a href="/logout/"><i class="fa fa-sign-out fa-fw"></i>Logout</a>\n    \t\t\t\t\t\t\t</li>\n    \t\t\t\t\t\t</ul>\n    \t\t\t\t\t<!-- /.dropdown-user -->\n    \t\t\t\t\t</li>\n')
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


def render_headlinks(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def headlinks():
            return render_headlinks(context)
        __M_writer = context.writer()
        __M_writer('\n    <!-- Custom Fonts -->\n\t<link href="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/thirdparties/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">\t    \n')
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


"""
__M_BEGIN_METADATA
{"filename": "/Users/scottromney/SiteOne/homepage/templates/base.htm", "line_map": {"128": 20, "65": 94, "130": 32, "131": 33, "132": 35, "133": 35, "134": 38, "71": 68, "136": 48, "137": 49, "138": 51, "77": 68, "143": 61, "208": 74, "83": 92, "148": 64, "196": 62, "214": 74, "153": 67, "89": 92, "27": 0, "135": 38, "158": 70, "95": 65, "163": 76, "101": 65, "129": 20, "169": 3, "107": 8, "178": 5, "176": 3, "177": 5, "50": 1, "190": 59, "220": 214, "55": 6, "184": 59, "202": 62, "60": 90, "125": 8, "126": 19, "127": 19}, "source_encoding": "ascii", "uri": "base.htm"}
__M_END_METADATA
"""
