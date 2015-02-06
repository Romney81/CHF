# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423250918.969836
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/administrator/templates/events.edit.html'
_template_uri = 'events.edit.html'
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
        eventform = context.get('eventform', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
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
        eventform = context.get('eventform', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div class="container">\n        <div class="manager-edit">\n            <div class="row">\n                <div class="panel panel-default col-md-12 col-sm-12">\n                    <div class="panel-heading">\n                        <h3 class="panel-title">Edit Event</h3>\n                    </div>\n                    <div class="panel-body">\n                        <form class="form-horizontal signin-form" method="POST">\n                            ')
        __M_writer(str( eventform.non_field_errors() ))
        __M_writer('\n                            ')
        __M_writer(str(eventform.media))
        __M_writer('\n')
        for field in eventform:
            __M_writer('                            <div class="form-group">\n                                <label class="col-md-2 control-label">')
            __M_writer(str(field.label))
            __M_writer('</label>\n                                <div class="col-md-8">\n                                    ')
            __M_writer(str(field))
            __M_writer('\n                                    <div class="form-constrol" style="padding-left: 0px">')
            __M_writer(str(field.errors))
            __M_writer('</div>\n                                </div>\n                            </div>\n')
        __M_writer('                            <div class="col-md-offset-2 col-md-2 save-btn-col">\n                                <button type="submit" class="btn btn-lg btn-white">Save</button>\n                            </div>\n                        </form>\n                    </div>\n                </div>\n            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"64": 20, "65": 20, "66": 24, "35": 1, "40": 33, "46": 3, "59": 16, "72": 66, "53": 3, "54": 13, "55": 13, "56": 14, "57": 14, "58": 15, "27": 0, "60": 17, "61": 17, "62": 19, "63": 19}, "filename": "/Users/scottromney/SiteOne/administrator/templates/events.edit.html", "uri": "events.edit.html"}
__M_END_METADATA
"""
