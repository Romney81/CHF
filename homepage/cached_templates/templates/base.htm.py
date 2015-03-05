# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425414335.669075
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['index', 'footlinks', 'headlinks', 'login', 'homepage', 'about', 'contact', 'content']


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
        def index():
            return render_index(context._locals(__M_locals))
        def footlinks():
            return render_footlinks(context._locals(__M_locals))
        def login():
            return render_login(context._locals(__M_locals))
        def homepage():
            return render_homepage(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        user = context.get('user', UNDEFINED)
        def about():
            return render_about(context._locals(__M_locals))
        def headlinks():
            return render_headlinks(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def contact():
            return render_contact(context._locals(__M_locals))
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
        __M_writer('\n\n            ')
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


def render_headlinks(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def headlinks():
            return render_headlinks(context)
        __M_writer = context.writer()
        __M_writer('\n    <!-- Custom Fonts -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_login(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def login():
            return render_login(context)
        __M_writer = context.writer()
        __M_writer('\n\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_homepage(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def index():
            return render_index(context)
        def login():
            return render_login(context)
        def homepage():
            return render_homepage(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        user = context.get('user', UNDEFINED)
        def about():
            return render_about(context)
        def content():
            return render_content(context)
        def contact():
            return render_contact(context)
        __M_writer = context.writer()
        __M_writer('\n    <div class="header">\n        <div class="navbar navbar-top navbar-fixed-top" role="navigation">\n            <div class="container">\n                <div class="navbar-header">\n                    <button type="button" class="navbar-toggle" data-toggle="offcanvas" data-target="collapse">\n                        <span class="icon-bar"></span>\n                        <span class="icon-bar"></span>\n                        <span class="icon-bar"></span>\n                    </button>\n                    <a class="navbar-brand" href="/index/">\n                        <img class="nav-logo" src="')
        __M_writer(str(STATIC_URL))
        __M_writer('/homepage/media/images/logo.svg" />\n                        <img class="nav-logo nav-logo-dark" src="')
        __M_writer(str(STATIC_URL))
        __M_writer('/homepage/media/images/logo-dark.svg" />\n                    </a>\n                </div>\n                <div id="navbar" class="navbar-collapse collapse">\n                    <ul class="nav navbar-nav mighthide">\n                        <li><a href="/index/">Home</a>\n                        </li>\n                        <li><a href="/about/">About</a>\n                        </li>\n                        <li><a href="/contact/">Contact</a>\n                        </li>\n                        <li><a href="/terms/">Terms</a>\n                        </li>\n                        <li><a href="/shop/">Shop</a>\n                        </li>\n                    </ul>\n                    <ul class="nav navbar-nav navbar-right">\n')
        if user.is_authenticated():
            __M_writer('                        <li class="dropdown">\n                            <a class="dropdown-toggle" data-toggle="dropdown" href="#">\n    \t\t\t\t\t\t\t')
            __M_writer(str(user.get_full_name()))
            __M_writer(' <i class="fa fa-user fa-fw"></i>  <i class="fa fa-caret-down"></i>\n    \t\t\t\t\t\t</a>\n                            <ul class="dropdown-menu dropdown-user">\n                                <li><a href="/administrator/"><i class="fa fa-user fa-fw"></i> ')
            __M_writer(str(user.get_full_name()))
            __M_writer('</a>\n                                </li>\n                                <li><a href="#"><i class="fa fa-gear fa-fw"></i> Settings</a>\n                                </li>\n                                <li class="divider"></li>\n                                <li><a href="/logout/"><i class="fa fa-sign-out fa-fw"></i>Logout</a>\n                                </li>\n                            </ul>\n                            <!-- /.dropdown-user -->\n                        </li>\n')
        else:
            __M_writer('                        <li><a href="/login/">Login</a>\n                        </li>\n')
        __M_writer('                    </ul>\n                </div>\n            </div>\n        </div>\n    </div>\n\n    <div id="homepage" class="container">\n        <div class="hero col-sm-12">\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'index'):
            context['self'].index(**pageargs)
        

        __M_writer('\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'login'):
            context['self'].login(**pageargs)
        

        __M_writer('\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'about'):
            context['self'].about(**pageargs)
        

        __M_writer('\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'contact'):
            context['self'].contact(**pageargs)
        

        __M_writer('\n        </div>\n        <!-- main area -->\n        <div class="col-xs-12 col-sm-12 main-content">\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n        </div>\n        <!-- /.col-xs-12 main -->\n    </div>\n    <!--/.container-->\n    <footer class="footer">\n        <div class="row">\n            <div class="col-md-4 col-md-offset-4 beta-signup">\n                <ul class="ccopyright">\n                    <li>All rights reserved.</li>\n                    <li><i class="fa fa-rebel"></i>\n                    </li>\n                    <li>Design: Scott Romney</li>\n                </ul>\n            </div>\n        </div>\n    </footer>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_about(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def about():
            return render_about(context)
        __M_writer = context.writer()
        __M_writer('\n\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_contact(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def contact():
            return render_contact(context)
        __M_writer = context.writer()
        __M_writer('\n\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/scottromney/SiteOne/homepage/templates/base.htm", "uri": "base.htm", "line_map": {"65": 102, "211": 79, "71": 64, "205": 79, "137": 7, "138": 18, "139": 18, "140": 19, "77": 64, "142": 36, "141": 19, "144": 39, "145": 39, "146": 42, "83": 100, "148": 52, "149": 53, "150": 56, "217": 211, "89": 100, "27": 0, "199": 73, "95": 3, "160": 69, "165": 72, "155": 66, "101": 3, "193": 73, "170": 75, "107": 67, "175": 81, "113": 67, "50": 1, "147": 42, "181": 70, "119": 7, "55": 5, "187": 70, "60": 98, "143": 37}, "source_encoding": "ascii"}
__M_END_METADATA
"""
