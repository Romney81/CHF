# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425518687.023509
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/shop/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['headlinks', 'footlinks', 'content', 'shop']


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
        def footlinks():
            return render_footlinks(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        def shop():
            return render_shop(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
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


def render_shop(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        user = context.get('user', UNDEFINED)
        def shop():
            return render_shop(context)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n    <nav class="navbar" role="navigation">\n        <div class="container-fluid">\n            <div class="navbar-header">\n                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar">\n                    <span class="sr-only">Toggle navigation</span>\n                    <span class="icon-bar"></span>\n                    <span class="icon-bar"></span>\n                    <span class="icon-bar"></span>\n                </button>\n                <a class="navbar-brand" href="#"></a>\n            </div>\n\n            <!-- Collect the nav links, forms, and other content for toggling -->\n            <div class="collapse navbar-collapse" id="navbar">\n                <ul class="nav navbar-nav">\n                    <li class="active"><a href="#">Home</a></li>\n                    <li><a href="#"></a></li>\n                </ul>\n                <form class="navbar-form navbar-left" role="search">\n                    <div class="form-group">\n                        <input type="text" class="form-control" placeholder="Search">\n                    </div>\n                    <button type="submit" class="btn btn-default">Submit</button>\n                </form>\n                <ul class="nav navbar-nav navbar-right">\n                    <li class="dropdown">\n                        <a class="dropdown-toggle btn" data-toggle="dropdown" href="#">\n                            <i class="fa fa-shopping-cart"></i> Cart (0)\n                        </a>\n                        <ul class="dropdown-menu dropdown-user">\n                            <li>\n                                <a href="/administrator/"><i class="fa fa-user fa-fw"></i>\n')
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
            __M_writer('                                <li><a id="login-modal-button" href="#"><i class="fa fa-user fa-fw"></i> Login</a>\n                                </li>\n                                <li><a href="/homepage/signup/"><i class="fa fa-user fa-fw"></i> Create Account</a>\n                                </li>\n')
        if user.is_authenticated():
            __M_writer('                            <li class="divider"></li>\n                            <li><a href="/logout/"><i class="fa fa-sign-out fa-fw"></i>Logout</a>\n                            </li>\n')
        __M_writer('                        </ul>\n                    </li>\n                </ul>\n\n            </div><!-- /.navbar-collapse -->\n        </div><!-- /.container-fluid -->\n    </nav>\n\n\n    <!-- LOGIN MODAL -->\n    <div class="modal custom fade" id="login-modal" tabindex="-1" role="dialog" aria-labelledby="" aria-hidden="true">\n        <div class="modal-dialog">\n            <div class="modal-content">\n                <div class="modal-body">\n\n                </div>\n            </div>\n        </div>\n    </div>\n\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"128": 75, "51": 98, "68": 3, "133": 97, "74": 100, "139": 133, "126": 70, "80": 100, "120": 57, "110": 41, "86": 95, "27": 0, "92": 95, "98": 7, "41": 1, "107": 7, "108": 40, "109": 41, "46": 5, "111": 41, "112": 42, "113": 43, "114": 45, "115": 54, "116": 55, "117": 55, "118": 55, "119": 56, "56": 102, "121": 59, "122": 61, "123": 62, "124": 64, "125": 65, "62": 3, "127": 71}, "filename": "/Users/scottromney/SiteOne/shop/templates/base.htm", "uri": "base.htm"}
__M_END_METADATA
"""
