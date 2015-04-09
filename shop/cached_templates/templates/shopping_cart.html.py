# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428616825.2668
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/shop/templates/shopping_cart.html'
_template_uri = 'shopping_cart.html'
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
        items = context.get('items', UNDEFINED)
        rentals = context.get('rentals', UNDEFINED)
        int = context.get('int', UNDEFINED)
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
        items = context.get('items', UNDEFINED)
        rentals = context.get('rentals', UNDEFINED)
        int = context.get('int', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\n\n<div class="item_container">\n')
        if items:
            __M_writer('    <h2>Purchases</h2>\n    <table class="table table-striped tcart">\n        <thead>\n\t\t\t<tr>\n\t\t\t  <th>Name</th>\n\t\t\t  <th>Quantity</th>\n\t\t\t  <th>Price</th>\n              <th>Item Total</th>\n              <th>Remove</th>\n\t\t\t</tr>\n\t\t</thead>\n\n        <tbody>\n            ')
            grand_total = 0 
            
            __M_writer('\n\n')
            for key,value in items.items():
                __M_writer('\n            ')

                price = int(value[0].value)
                qty = value[1]
                
                sub_total = (price * qty)
                grand_total += sub_total
                            
                
                __M_writer('\n\n\t\t\t<tr>\n\t\t\t  <td>')
                __M_writer(str(value[0].name))
                __M_writer('</td>\n\t\t\t  <td>')
                __M_writer(str(value[1]))
                __M_writer('</td>\n\t\t\t  <td>$')
                __M_writer(str(value[0].value))
                __M_writer('</td>\n              <td>$')
                __M_writer(str(sub_total))
                __M_writer('</td>\n              <td><a class="btn btn-danger delete_button" data-rental="False" data-pid="')
                __M_writer(str(value[0].id))
                __M_writer('" href="#"><i class="fa fa-times"></i></a></td>\n\t\t\t</tr>\n')
            __M_writer('\t\t</tbody>\n        <tfoot>\n            <tr>\n                <td><b>Total:</b> </td>\n                <td></td>\n                <td></td>\n                <td></td>\n                <td><b>$')
            __M_writer(str(grand_total))
            __M_writer('</b></td>\n            </tr>\n        </tfoot>\n    </table>\n')
        __M_writer('\n')
        if rentals:
            __M_writer('    <h2>Rentals</h2>\n    <table class="table table-striped tcart">\n        <thead>\n\t\t\t<tr>\n\t\t\t  <th>Name</th>\n              <th>Quantity</th>\n\t\t\t  <th>Price</th>\n              <th>Item Total</th>\n              <th>Remove</th>\n\t\t\t</tr>\n\t\t</thead>\n\n        <tbody>\n            ')
            grand_total = 0 
            
            __M_writer('\n\n')
            for rental in rentals:
                __M_writer('\n            ')

                price = rental.current_price
                
                sub_total = price * 30
                grand_total += sub_total
                            
                
                __M_writer('\n\t\t\t<tr>\n\t\t\t  <td>')
                __M_writer(str(rental.name))
                __M_writer('</td>\n              <td> RENT </td>\n\t\t\t  <td>$')
                __M_writer(str(rental.current_price))
                __M_writer('</td>\n              <td>$')
                __M_writer(str(sub_total))
                __M_writer('</td>\n              <td><a class="btn btn-danger delete_button" data-rental="True" data-pid="')
                __M_writer(str(rental.id))
                __M_writer('" href="#"><i class="fa fa-times"></i></a></td>\n\t\t\t</tr>\n')
            __M_writer('\t\t</tbody>\n        <tfoot>\n            <tr>\n                <td><b>Total:</b> </td>\n                <td></td>\n                <td></td>\n                <td></td>\n                <td><b>$')
            __M_writer(str(grand_total))
            __M_writer('</b></td>\n            </tr>\n        </tfoot>\n    </table>\n')
        if not rentals:
            if not items:
                __M_writer('            <div class="text-center">\n                <i class="fa fa-shopping-cart bigcart"></i>\n                <p>\n                    Shopping cart is empty! Get Shopping!\n                </p>\n            </div>\n')
        __M_writer('\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "shopping_cart.html", "line_map": {"27": 0, "37": 1, "42": 112, "48": 3, "57": 3, "58": 8, "59": 9, "60": 22, "62": 22, "63": 24, "64": 25, "65": 26, "73": 32, "74": 35, "75": 35, "76": 36, "77": 36, "78": 37, "79": 37, "80": 38, "81": 38, "82": 39, "83": 39, "84": 42, "85": 49, "86": 49, "87": 54, "88": 55, "89": 56, "90": 69, "92": 69, "93": 71, "94": 72, "95": 73, "102": 78, "103": 80, "104": 80, "105": 82, "106": 82, "107": 83, "108": 83, "109": 84, "110": 84, "111": 87, "112": 94, "113": 94, "114": 99, "115": 100, "116": 101, "117": 109, "123": 117}, "filename": "/Users/scottromney/SiteOne/shop/templates/shopping_cart.html"}
__M_END_METADATA
"""
