# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425790316.657471
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/shop/templates/confirmation.html'
_template_uri = 'confirmation.html'
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
        int = context.get('int', UNDEFINED)
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
        int = context.get('int', UNDEFINED)
        items = context.get('items', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n    <div class="confirmation">\n        <div class="container-fluid">\n            <div class="row">\n                <div class="col-md-6 col-md-offset-3">\n                    <!-- Title with number of items in shopping kart -->\n                    <h3 class="title">Thank You For Purchasing!</h3>\n                    <br />\n                    <div class="table-responsive">\n                        <!-- Table -->\n                        <table class="table tcart">\n                            <thead>\n                                <tr>\n                                    <th>#</th>\n                                    <th>Name</th>\n                                    <th>Image</th>\n                                    <th>Quantity</th>\n                                    <th>Unit Price</th>\n                                    <th>Total</th>\n                                </tr>\n                            </thead>\n                            <tbody>\n                                ')
        grand_total = 0 
        
        __M_writer('\n')
        for key,value in items.items():
            __M_writer('                                ')

            price = int(value[0].value)
            qty = value[1]
            
            sub_total = (price * qty)
            grand_total += sub_total
                                            
            
            __M_writer('\n                                <tr>\n                                    <!-- Index -->\n                                    <td>')
            __M_writer(str(value[0].id))
            __M_writer('</td>\n                                    <!-- Product  name -->\n                                    <td>')
            __M_writer(str(value[0].name))
            __M_writer('</td>\n                                    <!-- Product image -->\n                                    <td>\n                                        <a href="single-item.html">\n                                            <img src="')
            __M_writer(str(STATIC_URL))
            __M_writer('homepage/media/images/')
            __M_writer(str(value[0].id))
            __M_writer('.jpg" alt="" />\n                                        </a>\n                                    </td>\n                                    <!-- Quantity with refresh and remove button -->\n                                    <td>\n                                        ')
            __M_writer(str(value[1]))
            __M_writer('\n                                    </td>\n                                    <!-- Unit price -->\n                                    <td>$')
            __M_writer(str(value[0].value))
            __M_writer('</td>\n                                    <!-- Total cost -->\n                                    <td>$')
            __M_writer(str(sub_total))
            __M_writer('</td>\n                                </tr>\n')
        __M_writer('                                <tr>\n                                    <th></th>\n                                    <th></th>\n                                    <th></th>\n                                    <th></th>\n                                    <th>Total</th>\n                                    <th>$')
        __M_writer(str(grand_total))
        __M_writer('</th>\n                                </tr>\n                            </tbody>\n                        </table>\n                    </div>\n                    <div class="text-center">\n                        <h3>Purchase Process Comlete!</h3>\n                        <h4><a href="/shop/">Continue Shoping</a></h3>\n                    </div>\n\n                </div>\n            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/scottromney/SiteOne/shop/templates/confirmation.html", "line_map": {"71": 33, "72": 36, "73": 36, "74": 38, "75": 38, "76": 42, "77": 42, "78": 42, "79": 42, "80": 47, "81": 47, "82": 50, "83": 50, "84": 52, "85": 52, "86": 55, "87": 61, "88": 61, "27": 0, "94": 88, "37": 1, "42": 75, "48": 3, "57": 3, "58": 25, "60": 25, "61": 26, "62": 27, "63": 27}, "uri": "confirmation.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
