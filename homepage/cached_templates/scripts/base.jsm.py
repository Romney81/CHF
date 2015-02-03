# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422904178.594964
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
        __M_writer = context.writer()
        __M_writer("$(function(){\n    $('.navbar-default').data('size','big');\n});\n\n$(window).scroll(function(){\n    if($(document).scrollTop() > 0)\n    {\n        if($('.navbar-default').data('size') == 'big')\n        {\n            $('.navbar-default').data('size','small');\n            $('.navbar-default').stop().animate({\n                height:'40px'\n            },600);\n        }\n    }\n    else\n    {\n        if($('.navbar-default').data('size') == 'small')\n        {\n            $('.navbar-default').data('size','big');\n            $('.navbar-default').stop().animate({\n                height:'100px'\n            },600);\n        }  \n    }\n});\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/scottromney/SiteOne/homepage/scripts/base.jsm", "source_encoding": "ascii", "line_map": {"16": 0, "27": 21, "21": 1}, "uri": "base.jsm"}
__M_END_METADATA
"""
