# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422562211.176105
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/homepage/templates/manager.edit.html'
_template_uri = 'manager.edit.html'
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
        userform = context.get('userform', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        userform = context.get('userform', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n<div class="container">\n    <div class="manager-edit">\n        <form class="form-horizontal signin-form" method="POST">\n    \t\t')
        __M_writer(str( userform.non_field_errors() ))
        __M_writer('\n')
        for field in userform:
            __M_writer('    \t\t<div class="form-group">\n    \t\t\t<label class="col-md-2 control-label">')
            __M_writer(str(field.label))
            __M_writer('</label>\n    \t\t\t<div class="col-md-10">\n    \t\t\t\t')
            __M_writer(str(field))
            __M_writer(' \n    \t\t\t\t<div class="form-constrol" style="padding-left: 0px">')
            __M_writer(str(field.errors))
            __M_writer('</div>\n    \t\t\t</div>\n    \t\t</div>\n')
        __M_writer('    \t\t<div class="form-group col-md-12"> \n    \t\t\t<button type="submit" class="btn btn-lg btn-primary">Save</button>\n    \t\t</div>\n    \t</form>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "manager.edit.html", "source_encoding": "ascii", "filename": "/Users/scottromney/SiteOne/homepage/templates/manager.edit.html", "line_map": {"35": 1, "69": 63, "45": 3, "27": 0, "52": 3, "53": 7, "54": 7, "55": 8, "56": 9, "57": 10, "58": 10, "59": 12, "60": 12, "61": 13, "62": 13, "63": 17}}
__M_END_METADATA
"""
