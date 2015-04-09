# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428547525.05573
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/administrator/templates/overdue.html'
_template_uri = 'overdue.html'
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
        sixty = context.get('sixty', UNDEFINED)
        ninety = context.get('ninety', UNDEFINED)
        thirty = context.get('thirty', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        import datetime
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['datetime'] if __M_key in __M_locals_builtin_stored]))
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
        sixty = context.get('sixty', UNDEFINED)
        ninety = context.get('ninety', UNDEFINED)
        thirty = context.get('thirty', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div class="row">\n    \t<div class="col-lg-12">\n\t\t\t<div class="panel panel-default">\n                <div class="panel-heading">\n                    View Overdue Rentals\n                </div>\n                <!-- /.panel-heading -->\n                <div class="panel-body">\n                    <ul id="tabs" class="nav nav-tabs" data-tabs="tabs">\n                        <li class="active"><a href="#tabone" data-toggle="tab">Thirty Days</a></li>\n                        <li><a href="#tabtwo" data-toggle="tab">Sixty Days</a></li>\n                        <li><a href="#tabthree" data-toggle="tab">Ninety Days</a></li>\n                    </ul>\n                    <div id="my-tab-content" class="tab-content">\n                        <div class="tab-pane active" id="tabone">\n                            <div class="dataTable_wrapper">\n                                <table class="table table-striped table-bordered table-hover" id="thirty">\n                                    <thead>\n                                        <tr>\n                                            <th>ID</th>\n                                            <th>Name</th>\n                                            <th>Rental Date</th>\n                                            <th>Due Date</th>\n\n                                        </tr>\n                                    </thead>\n                                    <tbody>\n')
        for item in thirty:
            __M_writer('                                        <tr>\n                                            <td>')
            __M_writer(str(item.id))
            __M_writer('</td>\n                                            <td>')
            __M_writer(str(item.name))
            __M_writer('</td>\n                                            <td>')
            __M_writer(str(item.rental_date))
            __M_writer('</td>\n                                            <td>')
            __M_writer(str(item.due_date))
            __M_writer('</td>\n\n                                        </tr>\n')
        __M_writer('                                    </tbody>\n        \t\t\t\t\t    </table>\n                                <a data-email="30" class="btn btn-blue btn-email btn-thirty" href="#">Send Emails</a>\n                            </div>\n                        </div>\n                        <div class="tab-pane" id="tabtwo">\n                            <div class="dataTable_wrapper">\n                                <table class="table table-striped table-bordered table-hover" id="sixty">\n                                    <thead>\n                                        <tr>\n                                            <th>ID</th>\n                                            <th>Name</th>\n                                            <th>Rental Date</th>\n                                            <th>Due Date</th>\n\n                                        </tr>\n                                    </thead>\n                                    <tbody>\n')
        for item in sixty:
            __M_writer('                                        <tr>\n                                            <td>')
            __M_writer(str(item.id))
            __M_writer('</td>\n                                            <td>')
            __M_writer(str(item.name))
            __M_writer('</td>\n                                            <td>')
            __M_writer(str(item.rental_date))
            __M_writer('</td>\n                                            <td>')
            __M_writer(str(item.due_date))
            __M_writer('</td>\n\n                                        </tr>\n')
        __M_writer('                                    </tbody>\n        \t\t\t\t\t    </table>\n                                <a data-email="60" class="btn btn-blue btn-email btn-sixty" href="#">Send Emails</a>\n                            </div>\n                        </div>\n                        <div class="tab-pane" id="tabthree">\n                            <div class="dataTable_wrapper">\n                                <table class="table table-striped table-bordered table-hover" id="ninety">\n                                    <thead>\n                                        <tr>\n                                            <th>ID</th>\n                                            <th>Name</th>\n                                            <th>Rental Date</th>\n                                            <th>Due Date</th>\n\n                                        </tr>\n                                    </thead>\n                                    <tbody>\n')
        for item in ninety:
            __M_writer('                                        <tr>\n                                            <td>')
            __M_writer(str(item.id))
            __M_writer('</td>\n                                            <td>')
            __M_writer(str(item.name))
            __M_writer('</td>\n                                            <td>')
            __M_writer(str(item.rental_date))
            __M_writer('</td>\n                                            <td>')
            __M_writer(str(item.due_date))
            __M_writer('</td>\n                                        </tr>\n')
        __M_writer('                                    </tbody>\n        \t\t\t\t\t    </table>\n                                <a data-email="90" class="btn btn-blue btn-email btn-ninety" href="#">Send Emails</a>\n                            </div>\n                        </div>\n\n                    </div>\n                </div>\n                <!-- /.panel-body -->\n            </div>\n            <!-- /.panel -->\n        </div>\n        <!-- /.col-lg-12 -->\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 33, "65": 34, "66": 34, "67": 35, "68": 35, "69": 36, "70": 36, "71": 37, "72": 37, "73": 41, "74": 59, "75": 60, "76": 61, "77": 61, "78": 62, "79": 62, "80": 63, "81": 63, "82": 64, "83": 64, "84": 68, "85": 86, "86": 87, "87": 88, "88": 88, "89": 89, "90": 89, "27": 0, "92": 90, "93": 91, "94": 91, "95": 94, "91": 90, "37": 1, "38": 2, "42": 2, "47": 108, "53": 4, "101": 95, "62": 4, "63": 32}, "filename": "/Users/scottromney/SiteOne/administrator/templates/overdue.html", "source_encoding": "ascii", "uri": "overdue.html"}
__M_END_METADATA
"""
