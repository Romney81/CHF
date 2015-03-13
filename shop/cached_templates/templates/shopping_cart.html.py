# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425788479.457343
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
        items = context.get('items', UNDEFINED)
        int = context.get('int', UNDEFINED)
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
        int = context.get('int', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n\n<div class="item_container">\n    <table class="table table-striped tcart">\n\n        <thead>\n\t\t\t<tr>\n\t\t\t  <th>Name</th>\n\t\t\t  <th>Quantity</th>\n\t\t\t  <th>Price</th>\n              <th>Item Total</th>\n              <th>Remove</th>\n\t\t\t</tr>\n\t\t</thead>\n\n        <tbody>\n            ')
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
            __M_writer('</td>\n              <td><a class="btn btn-danger delete_button" data-pid="')
            __M_writer(str(value[0].id))
            __M_writer('" href="#"><i class="fa fa-times"></i></a></td>\n\t\t\t</tr>\n\n')
        __M_writer('\t\t</tbody>\n\n        <tfoot>\n            <tr>\n                <td><b>Total:</b> </td>\n                <td></td>\n                <td></td>\n                <td></td>\n                <td><b>$')
        __M_writer(str(grand_total))
        __M_writer('</b></td>\n            </tr>\n        </tfoot>\n\n    </table>\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/scottromney/SiteOne/shop/templates/shopping_cart.html", "uri": "shopping_cart.html", "line_map": {"69": 30, "70": 33, "71": 33, "72": 34, "73": 34, "74": 35, "75": 35, "76": 36, "77": 36, "78": 37, "79": 37, "80": 41, "81": 49, "82": 49, "88": 82, "27": 0, "36": 1, "41": 56, "47": 3, "55": 3, "56": 20, "58": 20, "59": 22, "60": 23, "61": 24}}
__M_END_METADATA
"""
