# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428546114.075232
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/shop/templates/item_details.html'
_template_uri = 'item_details.html'
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
        item = context.get('item', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        item = context.get('item', UNDEFINED)
        def content():
            return render_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <!-- <div class="container-fluid text-center">\n        <div class="col-md-3 col-md-offset-4">\n            <div class="panel panel-default">\n                <div class="panel-heading">\n                    <h3 class="panel-title">')
        __M_writer(str(item.name))
        __M_writer('</h3>\n                </div>\n                <div class="panel-body">\n\n                    <div class="item_image">\n                        <img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('/homepage/media/images/')
        __M_writer(str(item.id))
        __M_writer('.jpg" alt="" />\n                    </div>\n                    <p>\n                        ')
        __M_writer(str(item.description))
        __M_writer('\n\n                    </p>\n                    <p>\n                        ')
        __M_writer(str(item.value))
        __M_writer('\n                    </p>\n                    <div>\n                        <a data-pid="')
        __M_writer(str(item.id))
        __M_writer('" class="btn btn-blue add_button" href="#">Add to Cart</a>\n                    </div>\n                    <div class="dropdown">\n                        <select id="quantity" name="Item Quantity">\n                            <option value="1">1</option>\n                            <option value="2">2</option>\n                            <option value="3">3</option>\n                            <option value="4">4</option>\n                            <option value="5">5</option>\n                        </select>\n                    </div>\n                </div>\n            </div>\n        </div>\n    </div> -->\n    <!-- New Item Description -->\n    <div class="itemdetails">\n        <!-- Page Title -->\n\t\t<div class="section section-breadcrumbs">\n\t\t\t<div class="container">\n\t\t\t\t<div class="row">\n\t\t\t\t\t<div class="col-md-12">\n\t\t\t\t\t\t<h1>Product Details</h1>\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t</div>\n\n        <div class="section">\n\t    \t<div class="container">\n\t    \t\t<div class="row">\n\t    \t\t\t<!-- Product Image & Available Colors -->\n\t    \t\t\t<div class="col-sm-4">\n\t    \t\t\t\t<div class="product-image-large">\n\t    \t\t\t\t\t<img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('/homepage/media/images/')
        __M_writer(str(item.id))
        __M_writer('.jpg" alt="')
        __M_writer(str(item.name))
        __M_writer('">\n\t    \t\t\t\t</div>\n\t    \t\t\t\t<div class="colors">\n\t\t\t\t\t\t\t<span class="color-white"></span>\n\t\t\t\t\t\t\t<span class="color-black"></span>\n\t\t\t\t\t\t\t<span class="color-blue"></span>\n\t\t\t\t\t\t\t<span class="color-orange"></span>\n\t\t\t\t\t\t\t<span class="color-green"></span>\n\t\t\t\t\t\t</div>\n\t    \t\t\t</div>\n\t    \t\t\t<!-- End Product Image & Available Colors -->\n\t    \t\t\t<!-- Product Summary & Options -->\n\t    \t\t\t<div class="col-sm-6 product-details">\n\t    \t\t\t\t<h4>')
        __M_writer(str(item.name))
        __M_writer('</h4>\n                        <h5>Price</h5>\n\t    \t\t\t\t<p>\n                            $')
        __M_writer(str(item.value))
        __M_writer('\n\t    \t\t\t\t</p>\n\t\t\t\t\t\t<h5>Quick Overview</h5>\n\t    \t\t\t\t<p>\n                            ')
        __M_writer(str(item.description))
        __M_writer('\n\t    \t\t\t\t</p>\n                        <h5>Quantity</h5>\n                        <div class="dropdown">\n                            <select class="form-control selector" id="quantity" name="Item Quantity">\n                                <option value="1">1</option>\n                                <option value="2">2</option>\n                                <option value="3">3</option>\n                                <option value="4">4</option>\n                                <option value="5">5</option>\n                            </select>\n                        </div>\n                        <p>\n                            <a data-pid="')
        __M_writer(str(item.id))
        __M_writer('" data-rental="False" class="btn btn-blue add_button" href="#">Add to Cart</a>\n                        </p>\n\t    \t\t\t</div>\n\t    \t\t\t<!-- End Product Summary & Options -->\n\n\t    \t\t\t<!-- Full Description & Specification -->\n\t    \t\t\t<div class="col-sm-12">\n\t    \t\t\t\t<div class="tabbable">\n\t    \t\t\t\t\t<!-- Tabs -->\n\t\t\t\t\t\t\t<ul class="nav nav-tabs product-details-nav">\n\t\t\t\t\t\t\t\t<li class="active"><a href="#tab1" data-toggle="tab">Description</a></li>\n\t\t\t\t\t\t\t\t<li><a href="#tab2" data-toggle="tab">Specification</a></li>\n\t\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t\t<!-- Tab Content (Full Description) -->\n\t\t\t\t\t\t\t<div class="tab-content product-detail-info">\n\t\t\t\t\t\t\t\t<div class="tab-pane active" id="tab1">\n\t\t\t\t\t\t\t\t\t<h4>Product Description</h4>\n\t\t\t\t\t\t\t\t\t<p>\n\t\t\t\t\t\t\t\t\t\tDonec hendrerit massa metus, a ultrices elit iaculis eu. Pellentesque ullamcorper augue lacus. Phasellus et est quis diam iaculis fringilla id nec sapien. Sed tempor ornare felis, non vulputate dolor. Etiam ornare diam vitae ligula malesuada tempor. Vestibulum nec odio vel libero ullamcorper euismod et in sapien. Suspendisse potenti.\n\t\t\t\t\t\t\t\t\t</p>\n\t\t\t\t\t\t\t\t\t<h4>Product Highlights</h4>\n\t\t\t\t\t\t\t\t\t<ul>\n\t\t\t\t\t\t\t\t\t\t<li>Nullam dictum augue nec iaculis rhoncus. Aenean lobortis fringilla orci, vitae varius purus eleifend vitae.</li>\n\t\t\t\t\t\t\t\t\t\t<li>Nunc ornare, dolor a ultrices ultricies, magna dolor convallis enim, sed volutpat quam sem sed tellus.</li>\n\t\t\t\t\t\t\t\t\t\t<li>Aliquam malesuada cursus urna a rutrum. Ut ultricies facilisis suscipit.</li>\n\t\t\t\t\t\t\t\t\t\t<li>Duis a magna iaculis, aliquam metus in, luctus eros.</li>\n\t\t\t\t\t\t\t\t\t\t<li>Aenean nisi nibh, imperdiet sit amet eleifend et, gravida vitae sem.</li>\n\t\t\t\t\t\t\t\t\t\t<li>Donec quis nisi congue, ultricies massa ut, bibendum velit.</li>\n\t\t\t\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t\t\t\t<h4>Usage Information</h4>\n\t\t\t\t\t\t\t\t\t<p>\n\t\t\t\t\t\t\t\t\t\tDonec hendrerit massa metus, a ultrices elit iaculis eu. Pellentesque ullamcorper augue lacus. Phasellus et est quis diam iaculis fringilla id nec sapien. Sed tempor ornare felis, non vulputate dolor. Etiam ornare diam vitae ligula malesuada tempor. Vestibulum nec odio vel libero ullamcorper euismod et in sapien. Suspendisse potenti.\n\t\t\t\t\t\t\t\t\t</p>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t<!-- Tab Content (Specification) -->\n\t\t\t\t\t\t\t\t<div class="tab-pane" id="tab2">\n\t\t\t\t\t\t\t\t\t<table>\n\t\t\t\t\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t\t\t\t\t<td>Total sensor Pixels (megapixels)</td>\n\t\t\t\t\t\t\t\t\t\t\t<td>Approx. 16.7</td>\n\t\t\t\t\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t\t\t\t\t<td>Effective Pixels (megapixels)</td>\n\t\t\t\t\t\t\t\t\t\t\t<td>Approx. 16.1</td>\n\t\t\t\t\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t\t\t\t\t<td>Automatic White Balance</td>\n\t\t\t\t\t\t\t\t\t\t\t<td>YES</td>\n\t\t\t\t\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t\t\t\t\t<td>White balance: preset selection</td>\n\t\t\t\t\t\t\t\t\t\t\t<td>Daylight, Shade, Cloudy, Incandescent, Fluorescent, Flash</td>\n\t\t\t\t\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t\t\t\t\t<td>White balance: custom setting</td>\n\t\t\t\t\t\t\t\t\t\t\t<td>YES</td>\n\t\t\t\t\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t\t\t\t\t<td>White balance: types of color temperature</td>\n\t\t\t\t\t\t\t\t\t\t\t<td>YES (G7 to M7,15-step) (A7 to B7,15-step)</td>\n\t\t\t\t\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t\t\t\t\t<td>White balance bracketing</td>\n\t\t\t\t\t\t\t\t\t\t\t<td>NO</td>\n\t\t\t\t\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t\t\t\t\t<td>ISO Sensitivity Setting</td>\n\t\t\t\t\t\t\t\t\t\t\t<td>ISO100 - 25600 equivalent</td>\n\t\t\t\t\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t\t\t\t</table>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</div>\n\t    \t\t\t</div>\n\t    \t\t\t<!-- End Full Description & Specification -->\n\t    \t\t</div>\n\t\t\t</div>\n\t\t</div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 20, "65": 20, "66": 23, "67": 23, "68": 57, "69": 57, "70": 57, "71": 57, "72": 57, "73": 57, "74": 70, "75": 70, "76": 73, "77": 73, "78": 77, "79": 77, "80": 90, "81": 90, "87": 81, "27": 0, "36": 1, "41": 169, "47": 3, "55": 3, "56": 8, "57": 8, "58": 13, "59": 13, "60": 13, "61": 13, "62": 16, "63": 16}, "filename": "/Users/scottromney/SiteOne/shop/templates/item_details.html", "source_encoding": "ascii", "uri": "item_details.html"}
__M_END_METADATA
"""
