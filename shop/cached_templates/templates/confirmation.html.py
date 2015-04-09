# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428617136.516369
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
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        rentals = context.get('rentals', UNDEFINED)
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
        def content():
            return render_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        rentals = context.get('rentals', UNDEFINED)
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
        __M_writer('</th>\n                                </tr>\n                            </tbody>\n                        </table>\n                    </div>\n                    <div class="table-responsive">\n                        <!-- Table -->\n                        <table class="table tcart">\n                            <thead>\n                                <tr>\n                                    <th>#</th>\n                                    <th>Name</th>\n                                    <th>Image</th>\n                                    <th>Unit Price</th>\n                                    <th>Total</th>\n                                </tr>\n                            </thead>\n                            <tbody>\n                                ')
        grand_total = 0 
        
        __M_writer('\n')
        for rental in rentals:
            __M_writer('                                ')

            price = rental.current_price
            
            sub_total = price * 30
            grand_total += sub_total
                                            
            
            __M_writer('\n                                <tr>\n                                    <!-- Index -->\n                                    <td>')
            __M_writer(str(rental.id))
            __M_writer('</td>\n                                    <!-- Product  name -->\n                                    <td>')
            __M_writer(str(rental.name))
            __M_writer('</td>\n                                    <!-- Product image -->\n                                    <td>\n                                        <a href="single-item.html">\n                                            <img src="')
            __M_writer(str(STATIC_URL))
            __M_writer('homepage/media/images/rental')
            __M_writer(str(rental.id))
            __M_writer('.jpg" alt="" />\n                                        </a>\n                                    </td>\n                                    <!-- Unit price -->\n                                    <td>$')
            __M_writer(str(rental.current_price))
            __M_writer('</td>\n                                    <!-- Total cost -->\n                                    <td>$')
            __M_writer(str(sub_total))
            __M_writer('</td>\n                                </tr>\n')
        __M_writer('                                <tr>\n                                    <th></th>\n                                    <th></th>\n                                    <th></th>\n                                    <th></th>\n                                    <th>Total</th>\n                                    <th>$')
        __M_writer(str(grand_total))
        __M_writer('</th>\n                                </tr>\n\n                            </tbody>\n                        </table>\n                    </div>\n                    <div class="text-center">\n                        <h3>Purchase Process Complete!</h3>\n                        <h3>A Detailed Confirmation Email Is On Its Way!</h3>\n                        <h4><a href="/shop/">Continue Shoping</a></h3>\n                    </div>\n\n                </div>\n            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/scottromney/SiteOne/shop/templates/confirmation.html", "source_encoding": "ascii", "uri": "confirmation.html", "line_map": {"27": 0, "38": 1, "43": 126, "49": 3, "59": 3, "60": 25, "62": 25, "63": 26, "64": 27, "65": 27, "73": 33, "74": 36, "75": 36, "76": 38, "77": 38, "78": 42, "79": 42, "80": 42, "81": 42, "82": 47, "83": 47, "84": 50, "85": 50, "86": 52, "87": 52, "88": 55, "89": 61, "90": 61, "91": 79, "93": 79, "94": 80, "95": 81, "96": 81, "103": 86, "104": 89, "105": 89, "106": 91, "107": 91, "108": 95, "109": 95, "110": 95, "111": 95, "112": 99, "113": 99, "114": 101, "115": 101, "116": 104, "117": 110, "118": 110, "124": 118}}
__M_END_METADATA
"""
