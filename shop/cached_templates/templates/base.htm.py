# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425703533.146901
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/shop/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'headlinks', 'shop', 'footlinks']


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
        def footlinks():
            return render_footlinks(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def headlinks():
            return render_headlinks(context._locals(__M_locals))
        def shop():
            return render_shop(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'headlinks'):
            context['self'].headlinks(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'shop'):
            context['self'].shop(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footlinks'):
            context['self'].footlinks(**pageargs)
        

        __M_writer('\n')
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


def render_headlinks(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def headlinks():
            return render_headlinks(context)
        __M_writer = context.writer()
        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_shop(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        def shop():
            return render_shop(context)
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <nav class="navbar" role="navigation">\n        <div class="container-fluid">\n            <div class="navbar-header">\n                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar">\n                    <span class="sr-only">Toggle navigation</span>\n                    <span class="icon-bar"></span>\n                    <span class="icon-bar"></span>\n                    <span class="icon-bar"></span>\n                </button>\n                <a class="navbar-brand" href="#"></a>\n            </div>\n\n            <!-- Collect the nav links, forms, and other content for toggling -->\n            <div class="collapse navbar-collapse" id="navbar">\n                <ul class="nav navbar-nav">\n                    <li class="active"><a href="#">Home</a></li>\n                    <li><a href="#"></a></li>\n                </ul>\n                <form id="search_go" class="navbar-form navbar-left" method="POST" action="/shop/index.search/" >\n                    <div class="form-group">\n                        <input type="text" id="search_input" name="searchfield" class="form-control" placeholder="Search">\n                    </div>\n                    <button type="submit" id="search_button" class="btn btn-default">Submit</button>\n                </form>\n                <ul class="nav navbar-nav navbar-right">\n                    <li class="dropdown">\n                        <a class="dropdown-toggle btn" data-toggle="dropdown" href="#">\n                            <i class="fa fa-shopping-cart"></i> Cart (0)\n                        </a>\n                        <ul class="dropdown-menu dropdown-user">\n                            <li>\n                                <a class="cart-modal" href="#"><i class="fa fa-user fa-fw"></i>\n')
        if user.is_authenticated():
            __M_writer('                                        View ')
            __M_writer(str(user.first_name))
            __M_writer("'s Cart\n")
        else:
            __M_writer('                                        View Guest Cart\n')
        __M_writer('                                </a>\n                            </li>\n                        </ul>\n                    </li>\n                </ul>\n\n                <ul class="nav navbar-nav navbar-right">\n                    <li class="dropdown">\n                        <a class="dropdown-toggle btn" data-toggle="dropdown" href="#">\n')
        if user.is_authenticated():
            __M_writer('                                Hi, ')
            __M_writer(str(user.first_name))
            __M_writer('\n')
        else:
            __M_writer('                                Login or Signup\n')
        __M_writer('                        </a>\n                        <ul class="dropdown-menu dropdown-user">\n')
        if user.is_authenticated():
            __M_writer('                            <li><a href="/shop/account/"><i class="fa fa-gear fa-fw"></i> My Account</a>\n                            </li>\n')
        else:
            __M_writer('                                <li><a id="login-modal-button" href="#"><i class="fa fa-user fa-fw"></i> Login</a>\n                                </li>\n                                <li><a id="register-modal-button" href="#"><i class="fa fa-user fa-fw"></i> Create Account</a>\n                                </li>\n')
        if user.is_authenticated():
            __M_writer('                            <li class="divider"></li>\n                            <li><a href="/logout/"><i class="fa fa-sign-out fa-fw"></i>Logout</a>\n                            </li>\n')
        __M_writer('                        </ul>\n                    </li>\n                </ul>\n\n            </div><!-- /.navbar-collapse -->\n        </div><!-- /.container-fluid -->\n    </nav>\n\n\n    <!-- MODAL -->\n    <div class="modal custom fade" id="custom-modal" tabindex="-1" role="dialog" aria-labelledby="" aria-hidden="true">\n        <div class="modal-dialog">\n            <div class="modal-content">\n                <div class="modal-body">\n\n                </div>\n            </div>\n        </div>\n    </div>\n\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
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


"""
__M_BEGIN_METADATA
{"filename": "/Users/scottromney/SiteOne/shop/templates/base.htm", "source_encoding": "ascii", "uri": "base.htm", "line_map": {"115": 71, "68": 95, "133": 100, "74": 3, "139": 133, "80": 3, "110": 61, "86": 7, "27": 0, "95": 7, "96": 40, "97": 41, "98": 41, "99": 41, "100": 42, "101": 43, "102": 45, "103": 54, "104": 55, "41": 1, "106": 55, "107": 56, "108": 57, "109": 59, "46": 5, "111": 62, "112": 64, "113": 65, "114": 70, "51": 98, "116": 75, "105": 55, "56": 102, "121": 97, "62": 95, "127": 100}}
__M_END_METADATA
"""
