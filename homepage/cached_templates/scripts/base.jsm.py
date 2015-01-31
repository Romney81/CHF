# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422072506.666456
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/homepage/scripts/base.jsm'
_template_uri = 'base.jsm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        user_name = context.get('user_name', UNDEFINED)
        __M_writer = context.writer()
        __M_writer("$(function() {\n\tif('")
        __M_writer(str(user_name))
        __M_writer("' == 'Scott Romney'){\n    \t$('.mighthide').hide();\n    }\n\n});\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "base.jsm", "line_map": {"16": 0, "24": 2, "30": 24, "22": 1, "23": 2}, "filename": "/Users/scottromney/SiteOne/homepage/scripts/base.jsm", "source_encoding": "ascii"}
__M_END_METADATA
"""
