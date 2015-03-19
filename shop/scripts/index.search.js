$(function(){
    $('#search_go').ajaxForm(function(data){
        $('#item-loop').html(data);
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
                $('.button-panel').html("<a href=\"/shop/view-cart\" class=\"btn btn-blue pull-right\">View Cart</a>");
            },
            buttons:{
                "Checkout": function() {

                }
            },

        });
    });
});
