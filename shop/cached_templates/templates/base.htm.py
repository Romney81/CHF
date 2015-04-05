# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428210457.574228
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/shop/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['shop', 'footlinks', 'content', 'headlinks']


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
        def content():
            return render_content(context._locals(__M_locals))
        def shop():
            return render_shop(context._locals(__M_locals))
        def footlinks():
            return render_footlinks(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        def headlinks():
            return render_headlinks(context._locals(__M_locals))
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


def render_shop(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def shop():
            return render_shop(context)
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n    <nav class="navbar" role="navigation">\n        <div class="container-fluid">\n            <div class="navbar-header">\n                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar">\n                    <span class="sr-only">Toggle navigation</span>\n                    <span class="icon-bar"></span>\n                    <span class="icon-bar"></span>\n                    <span class="icon-bar"></span>\n                </button>\n                <a class="navbar-brand" href="#"></a>\n            </div>\n\n            <!-- Collect the nav links, forms, and other content for toggling -->\n            <div class="collapse navbar-collapse" id="navbar">\n                <ul class="nav navbar-nav">\n                    <li class="active"><a href="/homepage/">Homepage</a></li>\n                    <li class="active"><a href="/shop/">Shop</a></li>\n                    <li class="active"><a href="/shop/rentals/">Rentals</a></li>\n                    <li class="active"><a href="/shop/festivals/">Festivals</a></li>\n                    <li><a href="#"></a></li>\n                </ul>\n                <form id="search_go" class="navbar-form navbar-left" method="POST" action="/shop/index.search/" >\n                    <div class="form-group">\n                        <input type="text" id="search_input" name="searchfield" class="form-control" placeholder="Search">\n                    </div>\n                    <button type="submit" id="search_button" class="btn btn-default">Submit</button>\n                </form>\n                <ul class="nav navbar-nav navbar-right">\n                    <li class="dropdown">\n                        <a class="dropdown-toggle btn" data-toggle="dropdown" href="#">\n                            <i class="fa fa-shopping-cart"></i> Cart\n                        </a>\n                        <ul class="dropdown-menu dropdown-user">\n                            <li>\n                                <a class="cart-modal" href="#"><i class="fa fa-user fa-fw"></i>\n')
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
            __M_writer('                                <li><a id="login-modal-button" href="#"><i class="fa fa-user fa-fw"></i> Login</a>\n                                </li>\n                                <li><a id="register-modal-button" href="#"><i class="fa fa-user-plus fa-fw"></i> Create Account</a>\n                                </li>\n')
        if user.is_authenticated():
            __M_writer('                            <li class="divider"></li>\n                            <li><a href="/logout/"><i class="fa fa-sign-out fa-fw"></i>Logout</a>\n                            </li>\n')
        __M_writer('                        </ul>\n                    </li>\n                </ul>\n\n            </div><!-- /.navbar-collapse -->\n        </div><!-- /.container-fluid -->\n    </nav>\n\n\n\n    <!-- MODAL -->\n    <div class="modal custom fade" id="custom-modal" tabindex="-1" role="dialog" aria-labelledby="" aria-hidden="true">\n        <div class="modal-dialog">\n            <div class="modal-content">\n                <div class="modal-body">\n\n                </div>\n            </div>\n        </div>\n    </div>\n\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n    <!-- Footer starts -->\n\t\t<footer class="shop-footer">\n\t\t\t<div class="container">\n\t\t\t\t<div class="row">\n\t\t\t\t\t<div class="col-md-12">\n\t\t\t\t\t\t<div class="row">\n\t\t\t\t\t\t\t<div class="col-md-4">\n\t\t\t\t\t\t\t\t<div class="widget">\n\t\t\t\t\t\t\t\t\t<h5>Contact</h5>\n\t\t\t\t\t\t\t\t\t<hr />\n\t\t\t\t\t\t\t\t\t<div class="social">\n\t\t\t\t\t\t\t\t\t\t<a href="#"><i class="fa fa-facebook facebook"></i></a>\n\t\t\t\t\t\t\t\t\t\t<a href="#"><i class="fa fa-twitter twitter"></i></a>\n\t\t\t\t\t\t\t\t\t\t<a href="#"><i class="fa fa-linkedin linkedin"></i></a>\n\t\t\t\t\t\t\t\t\t\t<a href="#"><i class="fa fa-google-plus google-plus"></i></a>\n\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t<hr />\n\t\t\t\t\t\t\t\t\t<i class="fa fa-home"></i> &nbsp; 123, Some Area. Los Angeles, CA, 54321.\n\t\t\t\t\t\t\t\t\t<hr />\n\t\t\t\t\t\t\t\t\t<i class="fa fa-phone"></i> &nbsp; +239-3823-3434\n\t\t\t\t\t\t\t\t\t<hr />\n\t\t\t\t\t\t\t\t\t<i class="fa fa-envelope-o"></i> &nbsp; <a href="mailto:#">chf@colonialheritageutah.com</a>\n\t\t\t\t\t\t\t\t\t<hr />\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t<div class="col-md-4">\n\t\t\t\t\t\t\t\t<div class="widget">\n\t\t\t\t\t\t\t\t\t<h5>About Us</h5>\n\t\t\t\t\t\t\t\t\t<hr />\n\t\t\t\t\t\t\t\t\t<p>The Colonial Heritage Foundation (the Foundation) is a 501(c)(3) corporation dedicated to the preservation of the values, culture, skills and history of America\'s founding. To accomplish this mission, the Foundation engages in a broad array of activities.</p>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t<div class="col-md-4">\n\t\t\t\t\t\t\t\t<div class="widget">\n\t\t\t\t\t\t\t\t\t<h5>Common Links</h5>\n\t\t\t\t\t\t\t\t\t<hr />\n\t\t\t\t\t\t\t\t\t<div class="two-col">\n\t\t\t\t\t\t\t\t\t\t<div class="col-left">\n\t\t\t\t\t\t\t\t\t\t\t<ul>\n\t\t\t\t\t\t\t\t\t\t\t\t<li><a href="#">Home</a></li>\n\t\t\t\t\t\t\t\t\t\t\t\t<li><a href="#">Contact Us</a></li>\n\t\t\t\t\t\t\t\t\t\t\t\t<li><a href="#">Login</a></li>\n\n\t\t\t\t\t\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t<div class="col-right">\n\t\t\t\t\t\t\t\t\t\t\t<ul>\n                                                <li><a href="#">Register</a></li>\n\t\t\t\t\t\t\t\t\t\t\t\t<li><a href="#">Shop</a></li>\n\t\t\t\t\t\t\t\t\t\t\t\t<li><a href="#">Rentals</a></li>\n\t\t\t\t\t\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t<div class="clearfix"></div>\n\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t<hr />\n\t\t\t\t\t\t<!-- Copyright info -->\n\t\t\t\t\t\t<p class="copy">Copyright &copy; 2012 | <a href="#">Your Site</a> - <a href="#">Home</a> | <a href="#">About Us</a> | <a href="#">Service</a> | <a href="#">Contact Us</a></p>\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t<div class="clearfix"></div>\n\t\t\t</div>\n\t\t</footer>\n\t\t<!--/ Footer ends -->\n')
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


def render_headlinks(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def headlinks():
            return render_headlinks(context)
        __M_writer = context.writer()
        __M_writer('\n<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"115": 99, "133": 3, "71": 7, "72": 43, "73": 44, "74": 44, "75": 44, "76": 45, "77": 46, "78": 48, "79": 57, "80": 58, "81": 58, "82": 58, "83": 59, "84": 60, "85": 62, "86": 64, "87": 65, "88": 67, "89": 68, "90": 73, "27": 0, "92": 78, "97": 101, "91": 74, "139": 133, "103": 171, "41": 1, "109": 171, "46": 5, "51": 169, "56": 173, "121": 99, "62": 7, "127": 3}, "uri": "base.htm", "filename": "/Users/scottromney/SiteOne/shop/templates/base.htm"}
__M_END_METADATA
"""
