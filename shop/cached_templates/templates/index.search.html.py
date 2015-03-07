# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425703536.425837
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/shop/templates/index.search.html'
_template_uri = 'index.search.html'
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
    return runtime._inherit_from(context, 'base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        items = context.get('items', UNDEFINED)
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
        def content():
            return render_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        items = context.get('items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        for item in items:
            __M_writer('    <div class="col-md-3 col-sm-4">\n        <div class="item">\n            <!-- Item image -->\n            <div class="item-image">\n                <a href="/shop/item_details/')
            __M_writer(str(item.id))
            __M_writer('">\n                    <img src="')
            __M_writer(str(STATIC_URL))
            __M_writer('homepage/media/images/')
            __M_writer(str(item.id))
            __M_writer('.jpg" alt="" />\n                </a>\n            </div>\n            <!-- Item details -->\n            <div class="item-details">\n                <!-- Name -->\n                <!-- Use the span tag with the class "ico" and icon link (hot, sale, deal, new) -->\n                <h5><a href="single-item.html">')
            __M_writer(str(item.name))
            __M_writer('</a>\n                </h5>\n                <div class="clearfix"></div>\n                <!-- Para. Note more than 2 lines. -->\n                <p>')
            __M_writer(str(item.description))
            __M_writer('</p>\n                <hr />\n                <!-- Price -->\n                <div class="item-price pull-left">$')
            __M_writer(str(item.value))
            __M_writer('</div>\n                <!-- Add to cart -->\n                <div data-pid="')
            __M_writer(str(item.id))
            __M_writer('" class="button pull-right add_button"><a href="#">Add to Cart</a>\n                </div>\n                <div class="clearfix"></div>\n            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/scottromney/SiteOne/shop/templates/index.search.html", "source_encoding": "ascii", "uri": "index.search.html", "line_map": {"64": 17, "65": 17, "66": 21, "67": 21, "68": 24, "69": 24, "70": 26, "71": 26, "77": 71, "27": 0, "36": 1, "41": 33, "47": 3, "55": 3, "56": 4, "57": 5, "58": 9, "59": 9, "60": 10, "61": 10, "62": 10, "63": 10}}
__M_END_METADATA
"""
