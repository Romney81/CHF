# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428030830.251789
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/shop/templates/view-cart.html'
_template_uri = 'view-cart.html'
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
        item_count = context.get('item_count', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        rentals = context.get('rentals', UNDEFINED)
        items = context.get('items', UNDEFINED)
        int = context.get('int', UNDEFINED)
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
        item_count = context.get('item_count', UNDEFINED)
        def content():
            return render_content(context)
        rentals = context.get('rentals', UNDEFINED)
        items = context.get('items', UNDEFINED)
        int = context.get('int', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div class="cart">\n        <div class="container">\n            <div class="row">\n                <div class="col-md-10 col-md-offset-1">\n                    <!-- Title with number of items in shopping kart -->\n                    <h3 class="title"><i class="fa fa-shopping-cart"></i> Items in your cart [\n                        <span class="color">')
        __M_writer(str(item_count))
        __M_writer('</span> ]</h3>\n                    <br />\n                    <div class="table-responsive">\n                        <!-- Table -->\n                        <table class="table tcart">\n                            <thead>\n                                <tr>\n                                    <th>#</th>\n                                    <th>Name</th>\n                                    <th>Image</th>\n                                    <th>Quantity</th>\n                                    <th>Unit Price</th>\n                                    <th>Total</th>\n                                </tr>\n                            </thead>\n                            <tbody>\n                                ')
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
            __M_writer('.jpg" alt="" />\n                                        </a>\n                                    </td>\n                                    <!-- Quantity with refresh and remove button -->\n                                    <td class="item-input">\n                                        <div class="input-group">\n                                            <input class="form-control" type="text" value="1">\n                                            <span class="input-group-btn">\n                                                <button class="btn btn-default" type="button"><i class="fa fa-refresh"></i>\n                                                </button>\n                                                <button class="btn btn-danger" type="button"><i class="fa fa-times"></i>\n                                                </button>\n                                            </span>\n                                        </div>\n                                    </td>\n                                    <!-- Unit price -->\n                                    <td>$')
            __M_writer(str(value[0].value))
            __M_writer('</td>\n                                    <!-- Total cost -->\n                                    <td>$')
            __M_writer(str(sub_total))
            __M_writer('</td>\n                                </tr>\n')
        __M_writer('                                <tr>\n                                    <th></th>\n                                    <th></th>\n                                    <th></th>\n                                    <th></th>\n                                    <th>Total</th>\n                                    <th>$')
        __M_writer(str(grand_total))
        __M_writer('</th>\n                                </tr>\n\n                            </tbody>\n                        </table>\n                    </div>\n                    <div class="table-responsive">\n                        <!-- Table -->\n                        <table class="table tcart">\n                            <thead>\n                                <tr>\n                                    <th>#</th>\n                                    <th>Name</th>\n                                    <th>Image</th>\n                                    <th>Unit Price</th>\n                                    <th>Total</th>\n                                </tr>\n                            </thead>\n                            <tbody>\n                                ')
        grand_total = 0 
        
        __M_writer('\n')
        for rental in rentals:
            __M_writer('                                ')

            price = rental.current_price
            
            sub_total = price
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
        __M_writer('</th>\n                                </tr>\n\n                            </tbody>\n                        </table>\n                    </div>\n                    <h5 class="title">Gift Coupen</h5>\n                    <form class="form-inline">\n                <!-- Gift coupen -->\n\n                <div class="form-group">\n\t\t\t\t\t<input type="email" class="form-control" id="" placeholder="Gift Coupon">\n\t\t\t\t</div>\n\n\t\t\t\t<button type="submit" class="btn btn-default">Apply</button>\n              </form>\n\n               <!-- Button s-->\n              <div class="row">\n                <div class="col-md-5 col-md-offset-7">\n                  <div class="pull-right">\n                    <a href="/shop/" class="btn btn-default">Continue Shopping</a>\n                    <a href="/shop/checkout" class="btn btn-danger">CheckOut</a>\n                  </div>\n                </div>\n              </div>\n                </div>\n            </div>\n        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/scottromney/SiteOne/shop/templates/view-cart.html", "uri": "view-cart.html", "line_map": {"27": 0, "39": 1, "44": 149, "50": 3, "61": 3, "62": 10, "63": 10, "64": 26, "66": 26, "67": 27, "68": 28, "69": 28, "77": 34, "78": 37, "79": 37, "80": 39, "81": 39, "82": 43, "83": 43, "84": 43, "85": 43, "86": 59, "87": 59, "88": 61, "89": 61, "90": 64, "91": 70, "92": 70, "93": 89, "95": 89, "96": 90, "97": 91, "98": 91, "105": 96, "106": 99, "107": 99, "108": 101, "109": 101, "110": 105, "111": 105, "112": 105, "113": 105, "114": 109, "115": 109, "116": 111, "117": 111, "118": 114, "119": 120, "120": 120, "126": 120}}
__M_END_METADATA
"""
