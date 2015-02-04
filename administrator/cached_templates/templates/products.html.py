# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423017511.291457
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/administrator/templates/products.html'
_template_uri = 'products.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['admincontent']


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
    return runtime._inherit_from(context, 'index.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        products = context.get('products', UNDEFINED)
        def admincontent():
            return render_admincontent(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n<!-- Registered Users View -->  \n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'admincontent'):
            context['self'].admincontent(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_admincontent(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        products = context.get('products', UNDEFINED)
        def admincontent():
            return render_admincontent(context)
        __M_writer = context.writer()
        __M_writer(' \n    <div class="row manage manage-product">\n        <div class="col-lg-12">\n            <div class="panel panel-default">\n                <div class="panel-heading">\n                    Manage Products\n                </div>\n                <!-- /.panel-heading -->\n                <div class="panel-body">\n                    <div class="dataTable_wrapper">\n                        <table class="table table-striped table-bordered table-hover" id="data-table">\n                            <thead>\n                                <tr>\n                                    <th>ID</th>\n                                    <th>Product Name</th>\n                                    <th>Product Description</th>\n                                    <th>Product Category</th>\n                                    <th>Product Price</th>\n                                    <th>View/Edit Event</th>\n                                </tr>\n                            </thead>\n                            <tbody>\n')
        for product in products:
            __M_writer('                                <tr class="odd gradeX">\n                                    <td>')
            __M_writer(str(product.id))
            __M_writer('</td>\n                                    <td>')
            __M_writer(str(product.name))
            __M_writer('</td>\n                                    <td>')
            __M_writer(str(product.description))
            __M_writer('</td>\n                                    <td>')
            __M_writer(str(product.category))
            __M_writer('</td>\n                                    <td class="center">')
            __M_writer(str(product.current_price))
            __M_writer('</td>\n                                    <td class="center">\n                                        <a class="btn btn-info btn-xs" href="/administrator/products.edit/')
            __M_writer(str(product.id))
            __M_writer('/"><i class="fa fa-pencil-square-o"> Edit</i></a>\n                                        <a class="btn btn-danger btn-xs" href="/administrator/products.delete/')
            __M_writer(str(product.id))
            __M_writer('/"><i class="fa fa-times"> Delete</i></a>\n                                    </td>\n                                </tr>\n')
        __M_writer('                            </tbody>\n                        </table>\n                    </div>\n                    <!-- /.table-responsive -->\n                </div>\n                <!-- /.panel-body -->\n            </div>\n            <!-- /.panel -->\n        </div>\n        <!-- /.col-lg-12 -->\n    </div>\n    <!-- /.row --> \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 31, "65": 33, "66": 33, "67": 34, "68": 34, "69": 38, "75": 69, "27": 0, "35": 1, "45": 3, "52": 3, "53": 25, "54": 26, "55": 27, "56": 27, "57": 28, "58": 28, "59": 29, "60": 29, "61": 30, "62": 30, "63": 31}, "source_encoding": "ascii", "uri": "products.html", "filename": "/Users/scottromney/SiteOne/administrator/templates/products.html"}
__M_END_METADATA
"""
