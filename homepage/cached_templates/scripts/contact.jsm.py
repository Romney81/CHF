# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1421260667.191061
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/homepage/scripts/contact.jsm'
_template_uri = 'contact.jsm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('jQuery(function ($) {\n        function init_map1() {\n            var myLocation = new google.maps.LatLng(38.885516, -77.09327200000001);\n            var mapOptions = {\n                center: myLocation,\n                zoom: 16\n            };\n            var marker = new google.maps.Marker({\n                position: myLocation,\n                title: "Property Location"\n            });\n            var map = new google.maps.Map(document.getElementById("map1"),\n                mapOptions);\n            marker.setMap(map);\n        }\n        init_map1();\n    });')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"16": 0, "27": 21, "21": 1}, "filename": "/Users/scottromney/SiteOne/homepage/scripts/contact.jsm", "uri": "contact.jsm", "source_encoding": "ascii"}
__M_END_METADATA
"""
