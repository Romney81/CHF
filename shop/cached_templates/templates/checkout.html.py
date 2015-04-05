# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428094345.813701
_enable_loop = True
_template_filename = '/Users/scottromney/SiteOne/shop/templates/checkout.html'
_template_uri = 'checkout.html'
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
        form = context.get('form', UNDEFINED)
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
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\n\n    <div class="checkout">\n        <div class="container-fluid">\n            <div class="col-lg-6 col-lg-offset-3">\n                <div class="panel panel-default custom-panel">\n                    <div class="panel-body">\n                        <!-- Checkout page title -->\n                        <h4 class="title"><i class="fa fa-shopping-cart"></i> Checkout</h4>\n                        <!-- Sub title -->\n                        <h5 class="title">Shipping &amp; Billing Details</h5>\n                        <!-- Address and Shipping details form -->\n                        <div class="form form-small">\n                            <form class="form-horizontal" METHOD="POST">\n                                <div class="form-group">\n                                    <label class="control-label col-md-2" for="name1">')
        __M_writer(str( form['name'].label))
        __M_writer('</label>\n\n                                    <div class="col-md-8">\n                                        ')
        __M_writer(str( form['name']))
        __M_writer('\n                                        ')
        __M_writer(str( form['name'].errors))
        __M_writer('\n                                    </div>\n                                </div>\n                                <div class="form-group">\n                                    <label class="control-label col-md-2" for="name1">')
        __M_writer(str( form['email'].label))
        __M_writer('</label>\n                                    <div class="col-md-8">\n                                        ')
        __M_writer(str( form['email']))
        __M_writer('\n                                        ')
        __M_writer(str( form['email'].errors))
        __M_writer('\n                                    </div>\n                                </div>\n                                <div class="form-group">\n                                    <label class="control-label col-md-2" for="name1">')
        __M_writer(str( form['phone'].label))
        __M_writer('</label>\n                                    <div class="col-md-8">\n                                        ')
        __M_writer(str( form['phone']))
        __M_writer('\n                                        ')
        __M_writer(str( form['phone'].errors))
        __M_writer('\n                                    </div>\n                                </div>\n                                <div class="form-group">\n                                    <label class="control-label col-md-2" for="name1">')
        __M_writer(str( form['address'].label))
        __M_writer('</label>\n                                    <div class="col-md-8">\n                                        ')
        __M_writer(str( form['address']))
        __M_writer('\n                                        ')
        __M_writer(str( form['address'].errors))
        __M_writer('\n                                    </div>\n                                </div>\n                                <div class="form-group">\n                                    <label class="control-label col-md-2" for="name1">')
        __M_writer(str( form['country'].label))
        __M_writer('</label>\n                                    <div class="col-md-8">\n                                        ')
        __M_writer(str( form['country']))
        __M_writer('\n                                        ')
        __M_writer(str( form['country'].errors))
        __M_writer('\n                                    </div>\n                                </div>\n                                <div class="form-group">\n                                    <label class="control-label col-md-2" for="name1">')
        __M_writer(str( form['state'].label))
        __M_writer('</label>\n                                    <div class="col-md-8">\n                                        ')
        __M_writer(str( form['state']))
        __M_writer('\n                                        ')
        __M_writer(str( form['state'].errors))
        __M_writer('\n                                    </div>\n                                </div>\n                                <div class="form-group">\n                                    <label class="control-label col-md-2" for="name1">')
        __M_writer(str( form['city'].label))
        __M_writer('</label>\n                                    <div class="col-md-8">\n                                        ')
        __M_writer(str( form['city']))
        __M_writer('\n                                        ')
        __M_writer(str( form['city'].errors))
        __M_writer('\n                                    </div>\n\n                                </div>\n\n                                <hr />\n                                <!-- Payment details section -->\n                                <!-- Title -->\n                                <h5 class="title">Payment Details</h5>\n\n                                <div class="form-group">\n                                    <label class="control-label col-md-2" for="cardnumber">')
        __M_writer(str( form['ccname'].label))
        __M_writer('</label>\n                                    <div class="col-md-8">\n                                        ')
        __M_writer(str( form['ccname']))
        __M_writer('\n                                        ')
        __M_writer(str( form['ccname'].errors))
        __M_writer('\n                                    </div>\n                                </div>\n                                <div class="form-group">\n                                    <label class="control-label col-md-2" for="cardnumber">')
        __M_writer(str( form['cardnumber'].label))
        __M_writer('</label>\n                                    <div class="col-md-8">\n                                        ')
        __M_writer(str( form['cardnumber']))
        __M_writer('\n                                        ')
        __M_writer(str( form['cardnumber'].errors))
        __M_writer('\n                                    </div>\n                                </div>\n                                <div class="form-group">\n                                    <label class="control-label col-md-2" for="expdate">')
        __M_writer(str( form['expmonth'].label))
        __M_writer('</label>\n                                    <div class="col-md-6">\n                                        ')
        __M_writer(str( form['expmonth']))
        __M_writer('\n                                        ')
        __M_writer(str( form['expmonth'].errors))
        __M_writer('\n                                    </div>\n                                </div>\n                                <div class="form-group">\n                                    <label class="control-label col-md-2" for="expdate">')
        __M_writer(str( form['expyear'].label))
        __M_writer('</label>\n                                    <div class="col-md-6">\n                                        ')
        __M_writer(str( form['expyear']))
        __M_writer('\n                                        ')
        __M_writer(str( form['expyear'].errors))
        __M_writer('\n                                    </div>\n                                </div>\n                                <div class="form-group">\n                                    <label class="control-label col-md-2" for="expdate">')
        __M_writer(str( form['cvc'].label))
        __M_writer('</label>\n                                    <div class="col-md-6">\n                                        ')
        __M_writer(str( form['cvc']))
        __M_writer('\n                                        ')
        __M_writer(str( form['cvc'].errors))
        __M_writer('\n                                    </div>\n                                </div>\n                                <div class="row">\n                                    <div class="col-md-4 col-md-offset-8">\n                                        <div class="pull-right">\n                                            <button type="submit" class="btn btn-danger">Purchase</button>\n                                        </div>\n                                    </div>\n                                </div>\n                            </form>\n                        </div>\n                        <!-- Confirm order button -->\n                    </div>\n                </div>\n            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "checkout.html", "line_map": {"131": 125, "27": 0, "35": 1, "40": 126, "46": 3, "53": 3, "54": 20, "55": 20, "56": 23, "57": 23, "58": 24, "59": 24, "60": 28, "61": 28, "62": 30, "63": 30, "64": 31, "65": 31, "66": 35, "67": 35, "68": 37, "69": 37, "70": 38, "71": 38, "72": 42, "73": 42, "74": 44, "75": 44, "76": 45, "77": 45, "78": 49, "79": 49, "80": 51, "81": 51, "82": 52, "83": 52, "84": 56, "85": 56, "86": 58, "87": 58, "88": 59, "89": 59, "90": 63, "91": 63, "92": 65, "93": 65, "94": 66, "95": 66, "96": 77, "97": 77, "98": 79, "99": 79, "100": 80, "101": 80, "102": 84, "103": 84, "104": 86, "105": 86, "106": 87, "107": 87, "108": 91, "109": 91, "110": 93, "111": 93, "112": 94, "113": 94, "114": 98, "115": 98, "116": 100, "117": 100, "118": 101, "119": 101, "120": 105, "121": 105, "122": 107, "123": 107, "124": 108, "125": 108}, "source_encoding": "ascii", "filename": "/Users/scottromney/SiteOne/shop/templates/checkout.html"}
__M_END_METADATA
"""
