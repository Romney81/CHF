# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423693061.512538
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/administrator/templates/organizations.html'
_template_uri = 'organizations.html'
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
        organizations = context.get('organizations', UNDEFINED)
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
        organizations = context.get('organizations', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div class="row manage manage-product">\n        <div class="col-lg-12">\n            <div class="panel panel-default">\n                <div class="panel-heading">\n                    Manage Organizations <a href="/administrator/organizations.create/" class="btn-xs btn-primary pull-right"><i class="fa fa-plus-square-o"> Create New Organization</i></a>\n                </div>\n                <!-- /.panel-heading -->\n                <div class="panel-body">\n                    <div class="dataTable_wrapper">\n                        <table class="table table-striped table-bordered table-hover" id="data-table">\n                            <thead>\n                                <tr>\n                                    <th>ID</th>\n                                    <th>Type</th>\n                                    <th>Phone</th>\n                                    <th>Creation Date</th>\n                                    <th>Address</th>\n                                    <th>City</th>\n                                    <th>State</th>\n                                    <th>Zip</th>\n                                    <th>Email</th>\n                                    <th>Action</th>\n                                </tr>\n                            </thead>\n                            <tbody>\n')
        for organization in organizations:
            __M_writer('                                <tr class="odd gradeX">\n                                    <td>')
            __M_writer(str(organization.id))
            __M_writer('</td>\n                                    <td>')
            __M_writer(str(organization.organization_type))
            __M_writer('</td>\n                                    <td>')
            __M_writer(str(organization.phone))
            __M_writer('</td>\n                                    <td>')
            __M_writer(str(organization.creation_date))
            __M_writer('</td>\n                                    <td>')
            __M_writer(str(organization.address1))
            __M_writer('</td>\n                                    <td>')
            __M_writer(str(organization.city))
            __M_writer('</td>\n                                    <td>')
            __M_writer(str(organization.state))
            __M_writer('</td>\n                                    <td>')
            __M_writer(str(organization.zip_code))
            __M_writer('</td>\n                                    <td>')
            __M_writer(str(organization.email))
            __M_writer('</td>\n                                    <td class="text-center">\n                                        <a class="btn btn-info btn-xs" href="/administrator/organizations.edit/')
            __M_writer(str(organization.id))
            __M_writer('/"><i class="fa fa-pencil-square-o"> Edit</i></a>\n                                        <a class="btn btn-danger btn-xs" href="/administrator/organizations.delete/')
            __M_writer(str(organization.id))
            __M_writer('/"><i class="fa fa-times"> Delete</i></a>\n                                    </td>\n                                </tr>\n')
        __M_writer('                            </tbody>\n                        </table>\n                    </div>\n                    <!-- /.table-responsive -->\n                </div>\n                <!-- /.panel-body -->\n            </div>\n            <!-- /.panel -->\n        </div>\n        <!-- /.col-lg-12 -->\n    </div>\n    <!-- /.row -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "organizations.html", "source_encoding": "ascii", "line_map": {"64": 35, "65": 35, "66": 36, "67": 36, "68": 37, "69": 37, "70": 38, "71": 38, "72": 39, "73": 39, "74": 41, "75": 41, "76": 42, "77": 42, "78": 46, "84": 78, "27": 0, "35": 1, "40": 58, "46": 3, "53": 3, "54": 29, "55": 30, "56": 31, "57": 31, "58": 32, "59": 32, "60": 33, "61": 33, "62": 34, "63": 34}, "filename": "/Users/scottromney/SiteOne/administrator/templates/organizations.html"}
__M_END_METADATA
"""
