# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422663424.551315
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/homepage/templates/index.html'
_template_uri = 'index.html'
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
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\t\t\t<div class="hero col-sm-12">\n    \t\t\t<svg width="100%" height="143px" viewBox="0 0 1234 143" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:sketch="http://www.bohemiancoding.com/sketch/ns">\n                <title>Colonial Heritage Foundation</title>\n                <defs></defs>\n                    <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd" sketch:type="MSPage">\n                        <text id="Colonial-Heritage-Fo" sketch:type="MSTextLayer" font-family="Edwardian Script ITC" font-size="139" font-weight="normal" fill="#FFFFFF">\n                            <tspan x="-24" y="97">Colonial Heritage Foundation</tspan>\n                        </text>\n                    </g>\n                </svg>\n    \t\t\t<h2>Preserve the values, skills and history of Americas founding</h2>\n\t\t\t</div>\n          <div class="row">\n            <div class="col-sm-12"><h2>Reading and Discussion Groups</h2><p>\n              The Foundation coordinates and helps to establish community groups to encourage the reading and discussion of America\'s historical documents. For example, the Federalist Papers and the Anti-federalist Papers were publications that made the argument for and against the adoption of America\'s current constitution. The study and discussion of these documents can help Americans today understand the issues that were of most concern to our founding generation regarding the establishment of a strong federal government. These documents were written in a language style that is foreign to most contemporary readers. By providing recommended reading schedules, discussion questions, and materials to help modern readers read and grasp federal-period writings, the Foundation hopes to encourage small, community-based groups to undertake independent study of such founding documents. These discussion groups will be conducted year-round by volunteers and held in homes or community meeting places throughout the nation. \n              </p></div>\n          </div>\n          <hr>\n          <div class="row">\n            <div class="col-sm-12"><h2>Workshops, Lectures, and Seminars</h2><p>\n              The Foundation sponsors lectures, seminars and workshops about the values, culture, skills, and history of America\'s founding era. Such events may be coordinated with universities and other educationally-focused organizations to educate adults about the sacrifices that early Americans made to provide today\'s population with the freedoms we enjoy. These events  seek to inspire individuals to engage in community-based educational activities to increase exposure an awareness of the history surrounding America\'s founding. Lectures, seminars and workshops are coordinated and presented year-round by Foundation volunteers. Depending on the venue, they are offered either free of charge or for a fee.\n              </p></div>\n          </div>\n          <hr>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/scottromney/SiteOne/homepage/templates/index.html", "source_encoding": "ascii", "uri": "index.html", "line_map": {"56": 50, "34": 1, "27": 0, "44": 3, "50": 3}}
__M_END_METADATA
"""
