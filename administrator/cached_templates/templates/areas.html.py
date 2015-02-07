# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423276464.7939
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/administrator/templates/areas.html'
_template_uri = 'areas.html'
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
        areas = context.get('areas', UNDEFINED)
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
        areas = context.get('areas', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div class="row manage manage-product">\n        <div class="col-lg-12">\n            <div class="panel panel-default">\n                <div class="panel-heading">\n                    Manage Areas <a href="/administrator/areas.create/" class="btn-xs btn-primary pull-right"><i class="fa fa-plus-square-o"> Create New Area</i></a>\n                </div>\n                <!-- /.panel-heading -->\n                <div class="panel-body">\n                    <div class="dataTable_wrapper">\n                        <table class="table table-striped table-bordered table-hover" id="data-table">\n                            <thead>\n                                <tr>\n                                    <th>ID</th>\n                                    <th>Area Name</th>\n                                    <th>Area Description</th>\n                                    <th>View/Edit Event</th>\n                                </tr>\n                            </thead>\n                            <tbody>\n')
        for area in areas:
            __M_writer('                                <tr class="odd gradeX">\n                                    <td>')
            __M_writer(str(area.id))
            __M_writer('</td>\n                                    <td>')
            __M_writer(str(area.name))
            __M_writer('</td>\n                                    <td>')
            __M_writer(str(area.description))
            __M_writer('</td>\n                                    <td class="center">\n                                        <a class="btn btn-info btn-xs" href="/administrator/areas.edit/')
            __M_writer(str(area.id))
            __M_writer('/"><i class="fa fa-pencil-square-o"> Edit</i></a>\n                                        <a class="btn btn-danger btn-xs" href="/administrator/areas.delete/')
            __M_writer(str(area.id))
            __M_writer('/"><i class="fa fa-times"> Delete</i></a>\n                                    </td>\n                                </tr>\n')
        __M_writer('                            </tbody>\n                        </table>\n                    </div>\n                    <!-- /.table-responsive -->\n                </div>\n                <!-- /.panel-body -->\n            </div>\n            <!-- /.panel -->\n        </div>\n        <!-- /.col-lg-12 -->\n    </div>\n    <!-- /.row -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 30, "65": 30, "66": 34, "35": 1, "40": 46, "46": 3, "59": 26, "72": 66, "53": 3, "54": 23, "55": 24, "56": 25, "57": 25, "58": 26, "27": 0, "60": 27, "61": 27, "62": 29, "63": 29}, "filename": "/Users/scottromney/SiteOne/administrator/templates/areas.html", "source_encoding": "ascii", "uri": "areas.html"}
__M_END_METADATA
"""
