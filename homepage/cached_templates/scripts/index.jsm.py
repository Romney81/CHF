# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1421103297.510134
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/homepage/scripts/index.jsm'
_template_uri = 'index.jsm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer("$(function() {\n  // update the time every n seconds\n  window.setInterval(function() {\n    $('.browser-time').text('The current browser time is ' + new Date());\n  }, ")
        __M_writer(str( request.urlparams[1] if request.urlparams[1] else 500 ))
        __M_writer(');\n\n\t// update button\n\t$(\'#server-time-button\').click(function() {\n\t  $(\'.server-time\').load(\'/homepage/index.gettime\');\n\t});\n});\n\n    \n/*Menu-toggle*/\n$("#menu-toggle").click(function(e) {\n    e.preventDefault();\n    $("#wrapper").toggleClass("active");\n});\n\n/*Scroll Spy*/\n$(\'body\').scrollspy({ target: \'#spy\', offset:80});\n\n/*Smooth link animation*/\n$(\'a[href*=#]:not([href=#])\').click(function() {\n    if (location.pathname.replace(/^\\//, \'\') == this.pathname.replace(/^\\//, \'\') || location.hostname == this.hostname) {\n\n        var target = $(this.hash);\n        target = target.length ? target : $(\'[name=\' + this.hash.slice(1) + \']\');\n        if (target.length) {\n            $(\'html,body\').animate({\n                scrollTop: target.offset().top\n            }, 1000);\n            return false;\n        }\n    }\n});')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"16": 0, "24": 5, "30": 24, "22": 1, "23": 5}, "filename": "/Users/scottromney/SiteOne/homepage/scripts/index.jsm", "uri": "index.jsm", "source_encoding": "ascii"}
__M_END_METADATA
"""
