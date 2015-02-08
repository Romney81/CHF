# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423298763.872948
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/administrator/templates/items.html'
_template_uri = 'items.html'
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
        items = context.get('items', UNDEFINED)
        def admincontent():
            return render_admincontent(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n<!-- Registered Users View -->\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'admincontent'):
            context['self'].admincontent(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_admincontent(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        items = context.get('items', UNDEFINED)
        def admincontent():
            return render_admincontent(context)
        __M_writer = context.writer()
        __M_writer('\n <!-- Registered Items View -->\n    <div class="row manage manage-item">\n    \t<div class="col-lg-12">\n    \t\t<div class="panel panel-default">\n                <div class="panel-heading">\n                    Manage Items <a href="/administrator/items.create/" class="btn-xs btn-primary pull-right"><i class="fa fa-plus-square-o"> Create Item</i></a>\n                </div>\n                <!-- /.panel-heading -->\n                <div class="panel-body">\n                    <div class="dataTable_wrapper">\n                        <table class="table table-striped table-bordered table-hover" id="data-table">\n                            <thead>\n                                <tr>\n                                    <th>ID</th>\n                                    <th>Item Name</th>\n                                    <th>Item Description</th>\n                                    <th>Value</th>\n                                    <th>Is Rentable</th>\n                                    <th>Edit Item</th>\n                                </tr>\n                            </thead>\n                            <tbody>\n')
        for item in items:
            __M_writer('                                <tr class="odd gradeX">\n                                    <td>')
            __M_writer(str(item.id))
            __M_writer('</td>\n                                    <td>')
            __M_writer(str(item.name))
            __M_writer('</td>\n                                    <td>')
            __M_writer(str(item.description))
            __M_writer('</td>\n                                    <td>')
            __M_writer(str(item.value))
            __M_writer('</td>\n                                    <td class="center">')
            __M_writer(str(item.is_rentable))
            __M_writer('</td>\n                                    <td class="center">\n                                        <a class="btn btn-info btn-xs" href="/administrator/items.edit/')
            __M_writer(str(item.id))
            __M_writer('/"><i class="fa fa-pencil-square-o"> Edit</i></a>\n                                        <a class="btn btn-danger btn-xs" href="/administrator/items.delete/')
            __M_writer(str(item.id))
            __M_writer('/"><i class="fa fa-times"> Delete</i></a>\n                                    </td>\n                                </tr>\n')
        __M_writer('                            </tbody>\n\t\t\t\t\t\t</table>\n                    </div>\n                    <!-- /.table-responsive -->\n                </div>\n                <!-- /.panel-body -->\n            </div>\n            <!-- /.panel -->\n        </div>\n        <!-- /.col-lg-12 -->\n    </div>\n    <!-- /.row -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 32, "65": 32, "66": 34, "67": 34, "68": 35, "69": 35, "70": 39, "76": 70, "27": 0, "35": 1, "40": 51, "46": 3, "53": 3, "54": 26, "55": 27, "56": 28, "57": 28, "58": 29, "59": 29, "60": 30, "61": 30, "62": 31, "63": 31}, "source_encoding": "ascii", "uri": "items.html", "filename": "/Users/scottromney/SiteOne/administrator/templates/items.html"}
__M_END_METADATA
"""
