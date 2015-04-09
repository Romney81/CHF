# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428537837.445753
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
        rentals = context.get('rentals', UNDEFINED)
        int = context.get('int', UNDEFINED)
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
        rentals = context.get('rentals', UNDEFINED)
        int = context.get('int', UNDEFINED)
        items = context.get('items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\n\n<div class="item_container">\n')
        if items or rentals:
            __M_writer('    <table class="table table-striped tcart">\n        <thead>\n\t\t\t<tr>\n\t\t\t  <th>Name</th>\n\t\t\t  <th>Quantity</th>\n\t\t\t  <th>Price</th>\n              <th>Item Total</th>\n              <th>Remove</th>\n\t\t\t</tr>\n\t\t</thead>\n\n        <tbody>\n            ')
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
            __M_writer('</b></td>\n            </tr>\n        </tfoot>\n    </table>\n\n    <table class="table table-striped tcart">\n        <thead>\n\t\t\t<tr>\n\t\t\t  <th>Name</th>\n              <th>Quantity</th>\n\t\t\t  <th>Price</th>\n              <th>Item Total</th>\n              <th>Remove</th>\n\t\t\t</tr>\n\t\t</thead>\n\n        <tbody>\n            ')
            grand_total = 0 
            
            __M_writer('\n\n')
            for rental in rentals:
                __M_writer('\n            ')

                price = rental.current_price
                
                sub_total = price
                grand_total += sub_total
                            
                
                __M_writer('\n\t\t\t<tr>\n\t\t\t  <td>')
                __M_writer(str(rental.name))
                __M_writer('</td>\n              <td> - </td>\n\t\t\t  <td>$')
                __M_writer(str(rental.current_price))
                __M_writer('</td>\n              <td>$')
                __M_writer(str(sub_total))
                __M_writer('</td>\n              <td><a class="btn btn-danger delete_button" data-rental="True" data-pid="')
                __M_writer(str(rental.id))
                __M_writer('" href="#"><i class="fa fa-times"></i></a></td>\n\t\t\t</tr>\n')
            __M_writer('\t\t</tbody>\n        <tfoot>\n            <tr>\n                <td><b>Total:</b> </td>\n                <td></td>\n                <td></td>\n                <td></td>\n                <td><b>$')
            __M_writer(str(grand_total))
            __M_writer('</b></td>\n            </tr>\n        </tfoot>\n    </table>\n')
        else:
            __M_writer('    <div class="text-center">\n        <i class="fa fa-shopping-cart bigcart"></i>\n        <p>\n            Shopping cart is empty! Get Shopping!\n        </p>\n    </div>\n')
        __M_writer('\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"27": 0, "37": 1, "42": 105, "48": 3, "57": 3, "58": 8, "59": 9, "60": 21, "62": 21, "63": 23, "64": 24, "65": 25, "73": 31, "74": 34, "75": 34, "76": 35, "77": 35, "78": 36, "79": 36, "80": 37, "81": 37, "82": 38, "83": 38, "84": 41, "85": 48, "86": 48, "87": 65, "89": 65, "90": 67, "91": 68, "92": 69, "99": 74, "100": 76, "101": 76, "102": 78, "103": 78, "104": 79, "105": 79, "106": 80, "107": 80, "108": 83, "109": 90, "110": 90, "111": 94, "112": 95, "113": 102, "119": 113}, "uri": "shopping_cart.html", "filename": "/Users/scottromney/SiteOne/shop/templates/shopping_cart.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
