# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425520947.350658
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/shop/templates/account.html'
_template_uri = 'account.html'
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
        def content():
            return render_content(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
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
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div class="container-fluid">\n        <div class="col-lg-8 col-lg-offset-2">\n            <div class="panel with-nav-tabs account-container">\n                <div class="panel-heading">\n                    <ul class="nav nav-tabs">\n                        <li class="active"><a href="#tab1default" data-toggle="tab">My Information</a>\n                        </li>\n                        <li><a href="#tab2default" data-toggle="tab">Settings</a>\n                        </li>\n                    </ul>\n                </div>\n                <div class="panel-body">\n                    <div class="tab-content">\n                        <div class="tab-pane fade in active" id="tab1default">\n                            <div class="container">\n                                <label for="firstname" class="col-lg-2">First Name:</label>\n                                <div class="col-lg-10">\n                                    <p id="firstname">')
        __M_writer(str(user.first_name))
        __M_writer('</p>\n                                </div>\n                                <label for="lastname" class="col-lg-2">Last Name:</label>\n                                <div class="col-lg-10">\n                                    <p id="lastname">')
        __M_writer(str(user.last_name))
        __M_writer('</p>\n                                </div>\n                                <label for="email" class="col-lg-2">Email:</label>\n                                <div class="col-lg-10">\n                                    <p id="email">')
        __M_writer(str(user.email))
        __M_writer('</p>\n                                </div>\n                            </div>\n                        </div>\n                        <div class="tab-pane fade" id="tab2default">\n                            Default 2\n                        </div>\n                    </div>\n                </div>\n            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/scottromney/SiteOne/shop/templates/account.html", "line_map": {"65": 59, "35": 1, "40": 41, "46": 3, "59": 29, "53": 3, "54": 21, "55": 21, "56": 25, "57": 25, "58": 29, "27": 0}, "uri": "account.html"}
__M_END_METADATA
"""
