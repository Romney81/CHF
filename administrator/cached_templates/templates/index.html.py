# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423106422.409057
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/administrator/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['admincontent', 'content']


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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def admincontent():
            return render_admincontent(context._locals(__M_locals))
        countproducts = context.get('countproducts', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        user = context.get('user', UNDEFINED)
        countitems = context.get('countitems', UNDEFINED)
        countusers = context.get('countusers', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_admincontent(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def admincontent():
            return render_admincontent(context)
        countproducts = context.get('countproducts', UNDEFINED)
        countusers = context.get('countusers', UNDEFINED)
        countitems = context.get('countitems', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(' \n                \t<div class="row">\n                    \t<div class="col-lg-12">\n                        \t<h1 class="page-header">Admin</h1>\n    \t\t\t\t\t</div><!-- /.col-lg-12 -->\t\t\t\t\t\n    \t\t\t\t</div><!-- /.row -->\t\t\t\t\n    \t\t\t\t<div class="row">\n                    \t<div class="col-lg-3 col-md-6">\n                        \t<div class="panel panel-default">\n                            \t<div class="panel-heading">\n                                \t<div class="row">\n                                    \t<div class="col-xs-3">\n                                        \t<i class="fa fa-user fa-5x"></i>\n    \t\t\t\t\t\t\t\t\t</div>\n    \t\t\t\t\t\t\t\t\t<div class="col-xs-9 text-right">\n                                        \t<div class="huge">')
        __M_writer(str(countusers))
        __M_writer('</div>\n                                        <div>New User!</div>\n                                    </div>\n                                </div>\n                            </div>\n                            <a href="#">\n                                <div class="panel-footer">\n                                    <span class="pull-left">Create New User</span>\n                                    <span class="pull-right"><i class="fa fa-plus"></i></span>\n                                    <div class="clearfix"></div>\n                                </div>\n                            </a>\n                        </div>\n                    </div>\n                    <div class="col-lg-3 col-md-6">\n                        <div class="panel panel-default">\n                            <div class="panel-heading">\n                                <div class="row">\n                                    <div class="col-xs-3">\n                                        <i class="fa fa-flag fa-5x"></i>\n                                    </div>\n                                    <div class="col-xs-9 text-right">\n                                        <div class="huge">6</div>\n                                        <div>New Event!</div>\n                                    </div>\n                                </div>\n                            </div>\n                            <a href="#">\n                                <div class="panel-footer">\n                                    <span class="pull-left">Create New Event</span>\n                                    <span class="pull-right"><i class="fa fa-plus"></i></span>\n                                    <div class="clearfix"></div>\n                                </div>\n                            </a>\n                        </div>\n                    </div>\n                    <div class="col-lg-3 col-md-6">\n                        <div class="panel panel-default">\n                            <div class="panel-heading">\n                                <div class="row">\n                                    <div class="col-xs-3">\n                                        <i class="fa fa-plus-square-o fa-5x"></i>\n                                    </div>\n                                    <div class="col-xs-9 text-right">\n                                        <div class="huge">')
        __M_writer(str(countitems))
        __M_writer('</div>\n                                        <div>New Item!</div>\n                                    </div>\n                                </div>\n                            </div>\n                            <a href="#">\n                                <div class="panel-footer">\n                                    <span class="pull-left">Create New Item</span>\n                                    <span class="pull-right"><i class="fa fa-plus"></i></span>\n                                    <div class="clearfix"></div>\n                                </div>\n                            </a>\n                        </div>\n                    </div>\n                    <div class="col-lg-3 col-md-6">\n                        <div class="panel panel-default">\n                            <div class="panel-heading">\n                                <div class="row">\n                                    <div class="col-xs-3">\n                                        <i class="fa fa-shopping-cart fa-5x"></i>\n                                    </div>\n                                    <div class="col-xs-9 text-right">\n                                        <div class="huge">')
        __M_writer(str(countproducts))
        __M_writer('</div>\n                                        <div>New Product!</div>\n                                    </div>\n                                </div>\n                            </div>\n                            <a href="#">\n                                <div class="panel-footer">\n                                    <span class="pull-left">Create New Product</span>\n                                    <span class="pull-right"><i class="fa fa-plus"></i></span>\n                                    <div class="clearfix"></div>\n                                </div>\n                            </a>\n                        </div>\n                    </div>\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def admincontent():
            return render_admincontent(context)
        countproducts = context.get('countproducts', UNDEFINED)
        def content():
            return render_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        user = context.get('user', UNDEFINED)
        countitems = context.get('countitems', UNDEFINED)
        countusers = context.get('countusers', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div class="manager-view">\n\t\t<div id="wrapper">               \n            <div class="navbar sidebar" role="navigation"><!-- Navigation -->\n                <div class="sidebar-nav navbar-collapse">\n                    <div class="admin-profile">\n                        <img class="img-circle profile-image" src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/images/profile-pic.png" />\n                        <div class="profile-dropdown">\n                            <a class="dropdown-toggle" data-toggle="dropdown" href="#">\n        \t\t\t\t\t\t\t<i class="fa fa-user fa-fw"></i> ')
        __M_writer(str(user.get_full_name()))
        __M_writer('   <i class="fa fa-caret-down"></i>\n        \t\t\t\t\t\t</a>\n        \t\t\t\t\t\t<ul class="dropdown-menu dropdown-user">\n        \t\t\t\t\t\t\t<li><a href="/manager/"><i class="fa fa-user fa-fw"></i> ')
        __M_writer(str(user.get_full_name()))
        __M_writer('</a>\n        \t\t\t\t\t\t\t</li>\n        \t\t\t\t\t\t\t<li><a href="#"><i class="fa fa-gear fa-fw"></i> Settings</a>\n        \t\t\t\t\t\t\t</li>\n        \t\t\t\t\t\t\t<li class="divider"></li>\n        \t\t\t\t\t\t\t<li><a href="/logout/"><i class="fa fa-sign-out fa-fw"></i>Logout</a>\n        \t\t\t\t\t\t\t</li>\n        \t\t\t\t\t\t</ul>\n                        </div>\n                    </div>\n                    <ul class="nav" id="side-menu">\n                        <li>\n                            <a href="/administrator/"><i class="fa fa-dashboard fa-fw"></i> Dashboard</a>\n                        </li>\n                        <li>\n                            <a href="#"><i class="fa fa-user fa-fw"></i> Users<span class="fa arrow"></span></a>\n                            <ul class="nav nav-second-level">\n                                <li>\n                                    <a class="ru" href="/administrator/users/">Users</a>\n                                </li>                               \n                            </ul>\n                            <!-- /.nav-second-level -->\n                        </li>\n                        \n                        <li>\n                            <a class="event" href="/administrator/events/"><i class="fa fa-flag-o fa-fw"></i> Public Events</a>\n                        </li>\n                        <li>\n                            <a href="#"><i class="fa fa-cubes fa-fw"></i> Inventory<span class="fa arrow"></span></a>\n                            <ul class="nav nav-second-level">\n                                <li>\n                                    <a class="item" href="/administrator/items/">Items</a>\n                                </li>\n                                <li>\n                                    <a class="product" href="/administrator/products/">Products</a>\n                                </li>\n                            </ul>\n                            <!-- /.nav-second-level -->\n                        </li>\n                    </ul>\n                </div><!-- /.sidebar-collapse -->                \n            </div><!-- /.navbar-static-side -->\n            \n            <!--Main Page Content-->\n            <div id="page-wrapper">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'admincontent'):
            context['self'].admincontent(**pageargs)
        

        __M_writer(' \n            </div><!-- /.row -->              \n        </div>\n        <!-- /#page-wrapper -->\n    </div>\n    <!-- /#wrapper -->\n\t</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/scottromney/SiteOne/administrator/templates/index.html", "uri": "index.html", "line_map": {"64": 119, "65": 141, "66": 141, "91": 15, "102": 96, "72": 3, "41": 1, "96": 155, "51": 60, "85": 3, "86": 9, "87": 9, "88": 12, "89": 12, "90": 15, "27": 0, "60": 60, "61": 75, "62": 75, "63": 119}}
__M_END_METADATA
"""
