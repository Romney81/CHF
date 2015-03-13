# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425781664.203461
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/administrator/templates/overdue.html'
_template_uri = 'overdue.html'
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
        def admincontent():
            return render_admincontent(context._locals(__M_locals))
        items = context.get('items', UNDEFINED)
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
        def admincontent():
            return render_admincontent(context)
        items = context.get('items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div class="row">\n    \t<div class="col-lg-12">\n    \t\t\t<div class="panel panel-default">\n                    <div class="panel-heading">\n                        View Overdue Rentals\n                    </div>\n                    <!-- /.panel-heading -->\n                    <div class="panel-body">\n                        <div class="dataTable_wrapper">\n                            <table class="table table-striped table-bordered table-hover" id="data-table">\n                                <thead>\n                                    <tr>\n                                        <th>ID</th>\n                                        <th>Name</th>\n                                        <th>Rental Date</th>\n                                        <th>Due Date</th>\n\n                                    </tr>\n                                </thead>\n                                <tbody>\n')
        for item in items:
            __M_writer('                                    <tr>\n                                        <td>')
            __M_writer(str(item.id))
            __M_writer('</td>\n                                        <td>')
            __M_writer(str(item.name))
            __M_writer('</td>\n                                        <td>')
            __M_writer(str(item.rental_date))
            __M_writer('</td>\n                                        <td>')
            __M_writer(str(item.due_date))
            __M_writer('</td>\n\n                                    </tr>\n')
        __M_writer('                                </tbody>\n    \t\t\t\t\t</table>\n                    </div>\n                    <!-- /.table-responsive -->\n                </div>\n                <!-- /.panel-body -->\n            </div>\n            <!-- /.panel -->\n        </div>\n        <!-- /.col-lg-12 -->\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "overdue.html", "filename": "/Users/scottromney/SiteOne/administrator/templates/overdue.html", "line_map": {"64": 33, "35": 1, "70": 64, "40": 44, "46": 3, "59": 27, "53": 3, "54": 24, "55": 25, "56": 26, "57": 26, "58": 27, "27": 0, "60": 28, "61": 28, "62": 29, "63": 29}, "source_encoding": "ascii"}
__M_END_METADATA
"""
