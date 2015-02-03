# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422929853.378903
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/administrator/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


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
        countitems = context.get('countitems', UNDEFINED)
        items = context.get('items', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        products = context.get('products', UNDEFINED)
        countproducts = context.get('countproducts', UNDEFINED)
        countusers = context.get('countusers', UNDEFINED)
        users = context.get('users', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        countitems = context.get('countitems', UNDEFINED)
        items = context.get('items', UNDEFINED)
        def content():
            return render_content(context)
        products = context.get('products', UNDEFINED)
        countproducts = context.get('countproducts', UNDEFINED)
        countusers = context.get('countusers', UNDEFINED)
        users = context.get('users', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div class="manager-view">\n\t\t<div id="wrapper">               \n            <div class="navbar sidebar" role="navigation"><!-- Navigation -->\n                <div class="sidebar-nav navbar-collapse">\n                    <ul class="nav" id="side-menu">\n                        <li>\n                            <a href="/manager/"><i class="fa fa-dashboard fa-fw"></i> Dashboard</a>\n                        </li>\n                        <li>\n                            <a href="#"><i class="fa fa-user fa-fw"></i> Users<span class="fa arrow"></span></a>\n                            <ul class="nav nav-second-level">\n                                <li>\n                                    <a class="ru" href="#">Users</a>\n                                </li>                               \n                            </ul>\n                            <!-- /.nav-second-level -->\n                        </li>\n                        \n                        <li>\n                            <a class="event" href="#"><i class="fa fa-flag-o fa-fw"></i> Events</a>\n                        </li>\n                        <li>\n                            <a href="#"><i class="fa fa-cubes fa-fw"></i> Inventory<span class="fa arrow"></span></a>\n                            <ul class="nav nav-second-level">\n                                <li>\n                                    <a class="item" href="#">Items</a>\n                                </li>\n                                <li>\n                                    <a class="product" href="#">Products</a>\n                                </li>\n                            </ul>\n                            <!-- /.nav-second-level -->\n                        </li>\n                        <li>\n                            <a href="/logout/"><i class="fa fa-power-off fa-fw"></i> Logout</a>\n                        </li>\n                    </ul>\n                </div><!-- /.sidebar-collapse -->                \n            </div><!-- /.navbar-static-side -->\n            \n            <!--Main Page Content-->            \n\t\t\t<div id="page-wrapper">\n            \t<div class="row">\n                \t<div class="col-lg-12">\n                    \t<h1 class="page-header">Admin</h1>\n\t\t\t\t\t</div><!-- /.col-lg-12 -->\t\t\t\t\t\n\t\t\t\t</div><!-- /.row -->\t\t\t\t\n\t\t\t\t<div class="row">\n                \t<div class="col-lg-3 col-md-6">\n                    \t<div class="panel panel-default">\n                        \t<div class="panel-heading">\n                            \t<div class="row">\n                                \t<div class="col-xs-3">\n                                    \t<i class="fa fa-user fa-5x"></i>\n\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t<div class="col-xs-9 text-right">\n                                    \t<div class="huge">')
        __M_writer(str(countusers))
        __M_writer('</div>\n                                    <div>New User!</div>\n                                </div>\n                            </div>\n                        </div>\n                        <a href="#">\n                            <div class="panel-footer">\n                                <span class="pull-left">Create New User</span>\n                                <span class="pull-right"><i class="fa fa-plus"></i></span>\n                                <div class="clearfix"></div>\n                            </div>\n                        </a>\n                    </div>\n                </div>\n                <div class="col-lg-3 col-md-6">\n                    <div class="panel panel-default">\n                        <div class="panel-heading">\n                            <div class="row">\n                                <div class="col-xs-3">\n                                    <i class="fa fa-flag fa-5x"></i>\n                                </div>\n                                <div class="col-xs-9 text-right">\n                                    <div class="huge">6</div>\n                                    <div>New Event!</div>\n                                </div>\n                            </div>\n                        </div>\n                        <a href="#">\n                            <div class="panel-footer">\n                                <span class="pull-left">Create New Event</span>\n                                <span class="pull-right"><i class="fa fa-plus"></i></span>\n                                <div class="clearfix"></div>\n                            </div>\n                        </a>\n                    </div>\n                </div>\n                <div class="col-lg-3 col-md-6">\n                    <div class="panel panel-default">\n                        <div class="panel-heading">\n                            <div class="row">\n                                <div class="col-xs-3">\n                                    <i class="fa fa-plus-square-o fa-5x"></i>\n                                </div>\n                                <div class="col-xs-9 text-right">\n                                    <div class="huge">')
        __M_writer(str(countitems))
        __M_writer('</div>\n                                    <div>New Item!</div>\n                                </div>\n                            </div>\n                        </div>\n                        <a href="#">\n                            <div class="panel-footer">\n                                <span class="pull-left">Create New Item</span>\n                                <span class="pull-right"><i class="fa fa-plus"></i></span>\n                                <div class="clearfix"></div>\n                            </div>\n                        </a>\n                    </div>\n                </div>\n                <div class="col-lg-3 col-md-6">\n                    <div class="panel panel-default">\n                        <div class="panel-heading">\n                            <div class="row">\n                                <div class="col-xs-3">\n                                    <i class="fa fa-shopping-cart fa-5x"></i>\n                                </div>\n                                <div class="col-xs-9 text-right">\n                                    <div class="huge">')
        __M_writer(str(countproducts))
        __M_writer('</div>\n                                    <div>New Product!</div>\n                                </div>\n                            </div>\n                        </div>\n                        <a href="#">\n                            <div class="panel-footer">\n                                <span class="pull-left">Create New Product</span>\n                                <span class="pull-right"><i class="fa fa-plus"></i></span>\n                                <div class="clearfix"></div>\n                            </div>\n                        </a>\n                    </div>\n                </div>\n            </div><!-- /.row -->\n            \n            \n            \n            <!-- Registered Users View -->           \n            <div class="row manage manage-ru">\n            \t<div class="col-lg-12">\n            \t\t\t<div class="panel panel-default">\n                            <div class="panel-heading">\n                                Manage Users\n                            </div>\n                            <!-- /.panel-heading -->\n                            <div class="panel-body">\n                                <div class="dataTable_wrapper">\n                                    <table class="table table-striped table-bordered table-hover" id="users-table">\n                                        <thead>\n                                            <tr>\n                                                <th>ID</th>\n                                                <th>First Name</th>\n                                                <th>Last Name</th>\n                                                <th>Email</th>\n                                                <th>Address</th>\n                                                <th>City</th>\n                                                <th>State</th>\n                                                <th>Zip</th>\n                                                <th>Phone</th>\n                                                <th>Edit User</th>\n                                            </tr>\n                                        </thead>\n                                        <tbody> \n')
        for user in users:                           
            __M_writer('                                            <tr>\n                                                <td>')
            __M_writer(str(user.id))
            __M_writer('</td>\n                                                <td>')
            __M_writer(str(user.first_name))
            __M_writer('</td>\n                                                <td>')
            __M_writer(str(user.last_name))
            __M_writer('</td>\n                                                <td>')
            __M_writer(str(user.email))
            __M_writer('</td>\n                                                <td>')
            __M_writer(str(user.address))
            __M_writer('</td>\n                                                <td>')
            __M_writer(str(user.city))
            __M_writer('</td>\n                                                <td>')
            __M_writer(str(user.state))
            __M_writer('</td>\n                                                <td>')
            __M_writer(str(user.zip_code))
            __M_writer('</td>\n                                                <td>')
            __M_writer(str(user.phone))
            __M_writer('</td>\n                                                <td><a class="btn btn-default" href="/homepage/manager.edituser/')
            __M_writer(str(user.id))
            __M_writer('/">More Info/Edit User</a></td>\n                                            </tr>\n')
        __M_writer('                                        </tbody>\n        \t\t\t\t\t\t</table>\n                            </div>\n                            <!-- /.table-responsive -->\n                        </div>\n                        <!-- /.panel-body -->\n                    </div>\n                    <!-- /.panel -->\n                </div>\n                <!-- /.col-lg-12 -->\n            </div>\n            <!-- /.row -->\n            \n            <!-- Registered Users View -->           \n            <div class="row manage manage-event">\n            \t<div class="col-lg-12">\n            \t\t<div class="table-responsive">\n                        <table class="table responsive table-bordered table-hover table-striped">\n                            <thead>\n                                <tr>\n                                    <th><div class="btn btn-primary btn-large">Create New Event</div></th>                                   \n                                </tr>\n                            </thead>\n                            <thead>\n                                <tr>\n                                    <th>ID</th>\n                                    <th>Event Name</th>\n                                    <th>Event Location</th>\n                                    <th>View/Edit Event</th>\n                                </tr>\n                            </thead>\n                            <tbody>\n                                <tr>\n                                    <td>3326</td>\n                                    <td>Red Coat Rebellion</td>\n                                    <td>Provo, UT | <a href="#">Edit URL</a></td>\n                                    <td><a href="#">View/Edit Event</a></td>\n                                </tr>\n                                <tr>\n                                    <td>3326</td>\n                                    <td>Red Coat Rebellion</td>\n                                    <td>Provo, UT | <a href="#">Edit URL</a></td>\n                                    <td><a href="#">View/Edit Event</a></td>\n                                </tr>\n                                <tr>\n                                    <td>3326</td>\n                                    <td>Red Coat Rebellion</td>\n                                    <td>Provo, UT | <a href="#">Edit URL</a></td>\n                                    <td><a href="#">View/Edit Event</a></td>\n                                </tr>\n                                <tr>\n                                    <td>3326</td>\n                                    <td>Red Coat Rebellion</td>\n                                    <td>Provo, UT | <a href="#">Edit URL</a></td>\n                                    <td><a href="#">View/Edit Event</a></td>\n                                </tr>\n                            </tbody>\n\t\t\t\t\t\t</table>\n\t\t\t\t\t</div>\n                    <!-- /.table-responsive -->\n\t\t\t\t</div>                                    \n\t\t\t</div>\n            <!-- /.row -->\n            \n            \n            <!-- Registered Users View -->           \n            <div class="row manage manage-item">\n            \t<div class="col-lg-12">\n            \t\t<div class="panel panel-default">\n                        <div class="panel-heading">\n                            Manage Items\n                        </div>\n                        <!-- /.panel-heading -->\n                        <div class="panel-body">\n                            <div class="dataTable_wrapper">\n                                <table class="table table-striped table-bordered table-hover" id="items-table">\n                                    <thead>\n                                        <tr>\n                                            <th>ID</th>\n                                            <th>Item Name</th>\n                                            <th>Item Description</th>\n                                            <th>Value</th>\n                                            <th>Organization</th>\n                                            <th>Is Rentable</th>\n                                            <th>Edit Item</th>\n                                        </tr>\n                                    </thead>\n                                    <tbody>\n')
        for item in items:
            __M_writer('                                        <tr class="odd gradeX">\n                                            <td>')
            __M_writer(str(item.id))
            __M_writer('</td>\n                                            <td>')
            __M_writer(str(item.name))
            __M_writer('</td>\n                                            <td>')
            __M_writer(str(item.description))
            __M_writer('</td>\n                                            <td>')
            __M_writer(str(item.value))
            __M_writer('</td>\n                                            <td>')
            __M_writer(str(item.organization))
            __M_writer('</td>\n                                            <td class="center">')
            __M_writer(str(item.is_rentable))
            __M_writer('</td>\n                                            <td class="center"><a href="/homepage/manager.edititem/')
            __M_writer(str(item.id))
            __M_writer('/">View/Edit Item</a></td>\n                                        </tr>\n')
        __M_writer('                                    </tbody>\n        \t\t\t\t\t\t</table>\n                            </div>\n                            <!-- /.table-responsive -->\n                        </div>\n                        <!-- /.panel-body -->\n                    </div>\n                    <!-- /.panel -->\n                </div>\n                <!-- /.col-lg-12 -->\n            </div>\n            <!-- /.row -->   \n            \n            \n            <div class="row manage manage-product">\n                <div class="col-lg-12">\n                    <div class="panel panel-default">\n                        <div class="panel-heading">\n                            Manage Products\n                        </div>\n                        <!-- /.panel-heading -->\n                        <div class="panel-body">\n                            <div class="dataTable_wrapper">\n                                <table class="table table-striped table-bordered table-hover" id="products-table">\n                                    <thead>\n                                        <tr>\n                                            <th>ID</th>\n                                            <th>Product Name</th>\n                                            <th>Product Description</th>\n                                            <th>Product Category</th>\n                                            <th>Product Price</th>\n                                            <th>View/Edit Event</th>\n                                        </tr>\n                                    </thead>\n                                    <tbody>\n')
        for product in products:
            __M_writer('                                        <tr class="odd gradeX">\n                                            <td>')
            __M_writer(str(product.id))
            __M_writer('</td>\n                                            <td>')
            __M_writer(str(product.name))
            __M_writer('</td>\n                                            <td>')
            __M_writer(str(product.description))
            __M_writer('</td>\n                                            <td>')
            __M_writer(str(product.category))
            __M_writer('</td>\n                                            <td class="center">')
            __M_writer(str(product.current_price))
            __M_writer('</td>\n                                            <td class="center"><a href="#">View/Edit Product</a></td>\n                                        </tr>\n')
        __M_writer('                                    </tbody>\n                                </table>\n                            </div>\n                            <!-- /.table-responsive -->\n                        </div>\n                        <!-- /.panel-body -->\n                    </div>\n                    <!-- /.panel -->\n                </div>\n                <!-- /.col-lg-12 -->\n            </div>\n            <!-- /.row -->       \n                                \n        </div>\n        <!-- /#page-wrapper -->\n    </div>\n    <!-- /#wrapper -->\n\t</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/scottromney/SiteOne/administrator/templates/index.html", "line_map": {"27": 0, "40": 1, "50": 3, "62": 3, "63": 60, "64": 60, "65": 104, "66": 104, "67": 126, "68": 126, "69": 170, "70": 171, "71": 172, "72": 172, "73": 173, "74": 173, "75": 174, "76": 174, "77": 175, "78": 175, "79": 176, "80": 176, "81": 177, "82": 177, "83": 178, "84": 178, "85": 179, "86": 179, "87": 180, "88": 180, "89": 181, "90": 181, "91": 184, "92": 272, "93": 273, "94": 274, "95": 274, "96": 275, "97": 275, "98": 276, "99": 276, "100": 277, "101": 277, "102": 278, "103": 278, "104": 279, "105": 279, "106": 280, "107": 280, "108": 283, "109": 318, "110": 319, "111": 320, "112": 320, "113": 321, "114": 321, "115": 322, "116": 322, "117": 323, "118": 323, "119": 324, "120": 324, "121": 328, "127": 121}, "uri": "index.html"}
__M_END_METADATA
"""
