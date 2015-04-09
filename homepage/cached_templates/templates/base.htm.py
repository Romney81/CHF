# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428534205.483689
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['index', 'homepage', 'footlinks', 'headlinks', 'login', 'contact', 'about', 'content']


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
        def homepage():
            return render_homepage(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def headlinks():
            return render_headlinks(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        def login():
            return render_login(context._locals(__M_locals))
        def footlinks():
            return render_footlinks(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def contact():
            return render_contact(context._locals(__M_locals))
        def about():
            return render_about(context._locals(__M_locals))
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


def render_homepage(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def index():
            return render_index(context)
        def homepage():
            return render_homepage(context)
        def content():
            return render_content(context)
        request = context.get('request', UNDEFINED)
        user = context.get('user', UNDEFINED)
        def login():
            return render_login(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def contact():
            return render_contact(context)
        def about():
            return render_about(context)
        __M_writer = context.writer()
        __M_writer('\n    <div class="header">\n        <div class="navbar navbar-top navbar-fixed-top" role="navigation">\n            <div class="container">\n                <div class="navbar-header">\n                    <button type="button" class="navbar-toggle" data-toggle="offcanvas" data-target="collapse">\n                        <span class="icon-bar"></span>\n                        <span class="icon-bar"></span>\n                        <span class="icon-bar"></span>\n                    </button>\n                    <a class="navbar-brand" href="/index/">\n                        <img class="nav-logo" src="')
        __M_writer(str(STATIC_URL))
        __M_writer('/homepage/media/images/logo.svg" />\n                        <img class="nav-logo nav-logo-dark" src="')
        __M_writer(str(STATIC_URL))
        __M_writer('/homepage/media/images/logo-dark.svg" />\n                    </a>\n                </div>\n                <div id="navbar" class="navbar-collapse collapse">\n                    <ul class="nav navbar-nav mighthide">\n                        <li><a href="/index/">Home</a>\n                        </li>\n                        <li><a href="/about/">About</a>\n                        </li>\n                        <li><a href="/contact/">Contact</a>\n                        </li>\n                        <li><a href="/terms/">Terms</a>\n                        </li>\n                        <li><a href="/shop/">Shop</a>\n                        </li>\n')
        if request.user.is_superuser:
            __M_writer('                        <li><a href="/administrator/">Admin</a>\n                        </li>\n')
        __M_writer('                    </ul>\n                    <ul class="nav navbar-nav navbar-right">\n')
        if user.is_authenticated():
            __M_writer('                        <li class="dropdown">\n                            <a class="dropdown-toggle" data-toggle="dropdown" href="#">\n    \t\t\t\t\t\t\t')
            __M_writer(str(user.get_full_name()))
            __M_writer(' <i class="fa fa-user fa-fw"></i>  <i class="fa fa-caret-down"></i>\n    \t\t\t\t\t\t</a>\n                            <ul class="dropdown-menu dropdown-user">\n                                <li><a href="/administrator/"><i class="fa fa-user fa-fw"></i> ')
            __M_writer(str(user.get_full_name()))
            __M_writer('</a>\n                                </li>\n                                <li class="divider"></li>\n                                <li><a href="/user_logout/"><i class="fa fa-sign-out fa-fw"></i>Logout</a>\n                                </li>\n                            </ul>\n                            <!-- /.dropdown-user -->\n                        </li>\n')
        else:
            __M_writer('                        <li><a id="login-modal-button" href="/login/">Login</a>\n                        </li>\n')
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
        

        __M_writer('\n        </div>\n        <!-- /.col-xs-12 main -->\n    </div>\n\n    <!-- MODAL -->\n    <div class="modal custom fade" id="custom-modal" tabindex="-1" role="dialog" aria-labelledby="" aria-hidden="true">\n        <div class="modal-dialog">\n            <div class="modal-content">\n                <div class="modal-body">\n\n                </div>\n            </div>\n        </div>\n    </div>\n    <!--/.container-->\n    <footer class="footer">\n        <div class="row">\n            <div class="col-md-4 col-md-offset-4 beta-signup">\n                <ul class="ccopyright">\n                    <li>All rights reserved.</li>\n                    <li><i class="fa fa-rebel"></i>\n                    </li>\n                    <li>Design: Scott Romney</li>\n                </ul>\n            </div>\n        </div>\n    </footer>\n')
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
{"source_encoding": "ascii", "filename": "/Users/scottromney/SiteOne/homepage/templates/base.htm", "uri": "base.htm", "line_map": {"192": 75, "51": 1, "66": 115, "134": 74, "129": 71, "72": 66, "139": 77, "204": 72, "78": 66, "144": 83, "210": 81, "84": 7, "174": 69, "150": 113, "216": 81, "27": 0, "156": 113, "222": 216, "162": 3, "198": 72, "103": 7, "104": 18, "105": 18, "106": 19, "107": 19, "108": 34, "109": 35, "110": 38, "111": 40, "112": 41, "113": 43, "114": 43, "115": 46, "116": 46, "117": 54, "118": 55, "119": 58, "56": 5, "180": 69, "186": 75, "168": 3, "124": 68, "61": 111}}
__M_END_METADATA
"""
