# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423106395.336948
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/administrator/templates/events.html'
_template_uri = 'events.html'
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
        events = context.get('events', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<!-- Registered Users View -->  \n')
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
        events = context.get('events', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('         \n    <div class="row">\n    \t<div class="col-lg-12">\n    \t\t\t<div class="panel panel-default">\n                    <div class="panel-heading">\n                        Manage Public Events<a href="/administrator/events.create/" class="btn-xs btn-primary pull-right"><i class="fa fa-plus-square-o"> Create Public Event</i></a>\n                    </div>\n                    <!-- /.panel-heading -->\n                    <div class="panel-body">\n                        <div class="dataTable_wrapper">\n                            <table class="table table-striped table-bordered table-hover" id="data-table">\n                                <thead>\n                                    <tr>\n                                        <th>ID</th>\n                                        <th>Name</th>\n                                        <th>Description</th>\n                                        <th>Start Date</th>\n                                        <th>End Date</th>\n                                        <th>Action</th>\n                                    </tr>\n                                </thead>\n                                <tbody> \n')
        for event in events:                           
            __M_writer('                                    <tr>\n                                        <td>')
            __M_writer(str(event.id))
            __M_writer('</td>\n                                        <td>')
            __M_writer(str(event.name))
            __M_writer('</td>\n                                        <td>')
            __M_writer(str(event.description))
            __M_writer('</td>\n                                        <td>')
            __M_writer(str(event.start_date))
            __M_writer('</td>\n                                        <td>')
            __M_writer(str(event.end_date))
            __M_writer('</td>\n                                        <td class="text-center">\n                                            <a class="btn btn-info btn-xs" href="/administrator/events.edit/')
            __M_writer(str(event.id))
            __M_writer('/"><i class="fa fa-pencil-square-o"> Edit</i></a>\n                                            <a class="btn btn-danger btn-xs" href="/administrator/events.delete/')
            __M_writer(str(event.id))
            __M_writer('/"><i class="fa fa-times"> Delete</i></a>\n                                        </td>\n                                    </tr>\n')
        __M_writer('                                </tbody>\n    \t\t\t\t\t</table>\n                    </div>\n                    <!-- /.table-responsive -->\n                </div>\n                <!-- /.panel-body -->\n            </div>\n            <!-- /.panel -->\n        </div>\n        <!-- /.col-lg-12 -->\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/scottromney/SiteOne/administrator/templates/events.html", "uri": "events.html", "line_map": {"64": 31, "65": 31, "66": 33, "67": 33, "68": 34, "69": 34, "70": 38, "76": 70, "27": 0, "35": 1, "40": 49, "46": 3, "53": 3, "54": 25, "55": 26, "56": 27, "57": 27, "58": 28, "59": 28, "60": 29, "61": 29, "62": 30, "63": 30}}
__M_END_METADATA
"""
