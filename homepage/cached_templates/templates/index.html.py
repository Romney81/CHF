# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422926075.560878
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'index']


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
        def index():
            return render_index(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'index'):
            context['self'].index(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n    <div class="indexcontent">\n        <div class="row">\n            <div class="col-sm-12 text-center">\n                <h2>Reading and Discussion Groups</h2>\n            </div>\n        </div>\n        <hr>\n        <div class="row">\n            <div class="col-sm-12 text-center">\n                <h2>Workshops, Lectures, and Seminars</h2>\n            </div>\n        </div>\n        <hr>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_index(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def index():
            return render_index(context)
        __M_writer = context.writer()
        __M_writer('\n    <div class="hero-index">\n        <div class="col-sm-12 text-center">\n        <svg width="100%" height="146px" viewBox="0 0 1259 146" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:sketch="http://www.bohemiancoding.com/sketch/ns">\n            <defs></defs>\n            <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd" sketch:type="MSPage">\n                <text id="Colonial-Heritage-Fo" sketch:type="MSTextLayer" font-family="Edwardian Script ITC" font-size="139" font-weight="normal" fill="#FFF">\n                    <tspan x="-10" y="100">Colonial Heritage Foundation</tspan>\n                </text>\n            </g>\n        </svg>\n        <h2>Preserve the values, skills and history of Americas founding</h2>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/scottromney/SiteOne/homepage/templates/index.html", "line_map": {"75": 69, "51": 19, "36": 1, "69": 3, "57": 19, "41": 17, "27": 0, "63": 3}, "uri": "index.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
