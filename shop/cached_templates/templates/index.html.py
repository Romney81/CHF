# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425761872.479042
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/shop/templates/index.html'
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
        items = context.get('items', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
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
        items = context.get('items', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n    <!-- Content -->\n    <div class="items">\n        <div class="container">\n            <div class="row">\n                <div class="col-md-12">\n                    <h3 class="title">Popular Deals</h3>\n                </div>\n                <div id="item-loop">\n')
        for item in items:
            __M_writer('                    <div class="col-md-3 col-sm-4">\n                        <div class="item">\n                            <!-- Item image -->\n                            <div class="item-image">\n                                <a href="/shop/item_details/')
            __M_writer(str(item.id))
            __M_writer('">\n                                    <img src="')
            __M_writer(str(STATIC_URL))
            __M_writer('homepage/media/images/')
            __M_writer(str(item.id))
            __M_writer('.jpg" alt="" />\n                                </a>\n                            </div>\n                            <!-- Item details -->\n                            <div class="item-details">\n                                <!-- Name -->\n                                <!-- Use the span tag with the class "ico" and icon link (hot, sale, deal, new) -->\n                                <h5><a href="single-item.html">')
            __M_writer(str(item.name))
            __M_writer('</a>\n                                </h5>\n                                <div class="clearfix"></div>\n                                <!-- Para. Note more than 2 lines. -->\n                                <p>')
            __M_writer(str(item.description))
            __M_writer('</p>\n                                <hr />\n                                <!-- Price -->\n                                <div class="item-price pull-left">$')
            __M_writer(str(item.value))
            __M_writer('</div>\n                                <!-- Add to cart -->\n                                <div data-pid="')
            __M_writer(str(item.id))
            __M_writer('" class="button pull-right add_button"><a href="#"><i class="fa fa-cart-plus"></i> Add to Cart</a>\n                                </div>\n                                <div class="clearfix"></div>\n                            </div>\n                        </div>\n                    </div>\n')
        __M_writer('                </div>\n            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/scottromney/SiteOne/shop/templates/index.html", "source_encoding": "ascii", "line_map": {"64": 26, "65": 26, "66": 30, "67": 30, "68": 33, "69": 33, "70": 35, "71": 35, "72": 42, "78": 72, "27": 0, "36": 1, "41": 46, "47": 3, "55": 3, "56": 13, "57": 14, "58": 18, "59": 18, "60": 19, "61": 19, "62": 19, "63": 19}, "uri": "index.html"}
__M_END_METADATA
"""
