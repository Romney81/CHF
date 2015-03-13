$(function() {
    $('#custom-modal', '#register-modal').modal({
            show:false,
    });

    $('#login-modal-button').on('click', function() {
        event.preventDefault();
        $('#custom-modal').modal('show');
        $.ajax({
            url: '/shop/index.loginform',
            success: function (data) {
                $('#custom-modal').find('.modal-body').html(data);
            },

        });
    });

    $('#register-modal-button').on('click', function() {
        event.preventDefault();
        $('#custom-modal').modal('show');
        $.ajax({
            url: '/shop/index.registerform',
            success: function (data) {
                $('#custom-modal').find('.modal-body').html(data);
            },

        });
    });

    $('.add_button').on('click', function() {
        event.preventDefault();
        var pid = $(this).attr('data-pid');
        var qty = $('#quantity').val();

        if (! qty){
            qty = 1;
        }

        $.loadmodal({
            url: "/shop/shopping_cart.add/" + pid + "/" + qty,
            title: "Shopping Cart",
            width: "50%",
            onShow: function() {

                $('.button-panel').find('button').hide();
                $('.button-panel').css({"height": "40px"});
                $('.button-panel').html("<a href=\"/shop/checkout\" class=\"btn btn-blue pull-right\">Checkout</a>");
            },
            buttons:{
                "Checkout": function() {

                }
            },

        });
    });

    $('.cart-modal').on('click', function() {
        event.preventDefault();
        $.loadmodal({
            url: "/shop/shopping_cart/",
            title: "Shopping Cart",
            width: "50%",
            onShow: function() {

                $('.button-panel').find('button').hide();
                $('.button-panel').css({"height": "40px"});
                $('.button-panel').html("<a href=\"/shop/view-cart\" class=\"btn btn-blue pull-right\">View Cart</a>");
            },
            buttons:{
                "Checkout": function() {

                }
            },

        });
    });

    $('#search_button').click(function() {

        var input = $("#search_input").val()

        var options = {

            data:{
                'input': input,
            },

            success: function(data) {
                $('#item-loop').html(data);
            }
        }

        $('#search_go').ajaxForm(options);
    });

});
