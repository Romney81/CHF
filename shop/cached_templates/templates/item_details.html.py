# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425693762.016353
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        item = context.get('item', UNDEFINED)
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        item = context.get('item', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n    <div class="container-fluid">\n        <div class="col-md-6 col-md-offset-2">\n            <div class="panel panel-default">\n                <div class="panel-heading">\n                    <h3 class="panel-title">')
        __M_writer(str(item.name))
        __M_writer('</h3>\n                </div>\n                <div class="panel-body">\n\n                    <div class="item_image">\n                        <img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('/homepage/media/images/')
        __M_writer(str(item.id))
        __M_writer('.jpg" alt="" />\n                    </div>\n                    <p>\n                        ')
        __M_writer(str(item.description))
        __M_writer('\n\n                    </p>\n                    <p>\n                        ')
        __M_writer(str(item.value))
        __M_writer('\n                    </p>\n                    <div data-pid="')
        __M_writer(str(item.id))
        __M_writer('" class="btn btn-blue add_button">\n                        <a href="#">Add to Cart</a>\n                    </div>\n                    <div class="dropdown">\n                        <select id="quantity" name="Item Quantity">\n                            <option value="1">1</option>\n                            <option value="2">2</option>\n                            <option value="3">3</option>\n                            <option value="4">4</option>\n                            <option value="5">5</option>\n                        </select>\n                    </div>\n\n                </div>\n\n            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 20, "65": 20, "66": 22, "27": 0, "36": 1, "41": 40, "47": 3, "67": 22, "73": 67, "55": 3, "56": 8, "57": 8, "58": 13, "59": 13, "60": 13, "61": 13, "62": 16, "63": 16}, "uri": "item_details.html", "source_encoding": "ascii", "filename": "/Users/scottromney/SiteOne/shop/templates/item_details.html"}
__M_END_METADATA
"""
