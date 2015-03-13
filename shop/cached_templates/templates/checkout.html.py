# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425791534.270061
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
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
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
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n\n\n    <div class="checkout">\n        <div class="container-fluid">\n            <div class="col-lg-6 col-lg-offset-3">\n                <div class="panel panel-default custom-panel">\n                    <div class="panel-body">\n                        <!-- Checkout page title -->\n                        <h4 class="title"><i class="fa fa-shopping-cart"></i> Checkout</h4>\n                        <!-- Sub title -->\n                        <h5 class="title">Shipping &amp; Billing Details</h5>\n                        <!-- Address and Shipping details form -->\n                        <div class="form form-small">\n                            <form class="form-horizontal">\n')
        for field in form:
            __M_writer('                                <div class="form-group">\n\n                                    <label class="control-label col-md-2" for="name1">')
            __M_writer(str(field.label))
            __M_writer('</label>\n                                    <div class="col-md-8">\n                                        ')
            __M_writer(str(field))
            __M_writer('\n                                    </div>\n                                </div>\n')
        __M_writer('                            </form>\n                        </div>\n                        <hr />\n                        <!-- Payment details section -->\n                        <!-- Title -->\n                        <h5 class="title">Payment Details</h5>\n\n                        <!-- Radio buttons to select payment type -->\n\n                        <label class="radio-inline">\n                            <input type="radio" name="optionsRadios" id="optionsRadios1" value="1" checked> Debit Card\n                        </label>\n                        <label class="radio-inline">\n                            <input type="radio" name="optionsRadios" id="optionsRadios2" value="2"> Credit Card\n                        </label>\n                        <label class="radio-inline">\n                            <input type="radio" name="optionsRadios" id="optionsRadios3" value="3"> Internet Banking\n                        </label>\n                        <label class="radio-inline">\n                            <input type="radio" name="optionsRadios" id="optionsRadios4" value="4"> Cash On Delivery\n                        </label>\n                        <label class="radio-inline">\n                            <input type="radio" name="optionsRadios" id="optionsRadios5" value="5"> Paypal\n                        </label>\n\n                        <hr />\n\n                        <div class="form form-small">\n                            <form class="form-horizontal">\n                                <div class="form-group">\n                                    <label class="control-label col-md-2" for="cardnumber">Name</label>\n                                    <div class="col-md-8">\n                                        <input type="text" class="form-control" id="cardnumber" placeholder="Full Name on Card">\n                                    </div>\n                                </div>\n                                <div class="form-group">\n                                    <label class="control-label col-md-2" for="cardnumber">Card Number</label>\n                                    <div class="col-md-8">\n                                        <input type="text" class="form-control" id="cardnumber" placeholder="0000-0000-0000-0000">\n                                    </div>\n                                </div>\n                                <div class="form-group">\n                                    <label class="control-label col-md-2" for="expdate">Expiration Date</label>\n                                    <div class="col-md-4">\n                                        <input type="text" class="form-control" id="expdate" placeholder="09/19/2019">\n                                    </div>\n                                </div>\n                                <div class="form-group">\n                                    <label class="control-label col-md-2" for="expdate">CVV</label>\n                                    <div class="col-md-2">\n                                        <input type="text" class="form-control" id="expdate" placeholder="801">\n                                    </div>\n                                </div>\n                            </form>\n                        </div>\n\n                        <!-- Confirm order button -->\n                        <div class="row">\n                            <div class="col-md-4 col-md-offset-8">\n                                <div class="pull-right">\n                                    <a href="/shop/checkout.confirmation/" class="btn btn-danger">Purchase</a>\n                                </div>\n                            </div>\n                        </div>\n                    </div>\n                </div>\n            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "checkout.html", "filename": "/Users/scottromney/SiteOne/shop/templates/checkout.html", "source_encoding": "ascii", "line_map": {"66": 60, "35": 1, "40": 97, "46": 3, "59": 24, "53": 3, "54": 19, "55": 20, "56": 22, "57": 22, "58": 24, "27": 0, "60": 28}}
__M_END_METADATA
"""
