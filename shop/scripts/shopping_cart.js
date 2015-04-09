$('.delete_button').on('click', function() {
    event.preventDefault();
    var pid = $(this).attr('data-pid');
    var rent = $(this).attr('data-rental');

    console.log(pid)
    console.log(rent)

    $.loadmodal({
        url: "/shop/shopping_cart.delete/" + pid + "/" + rent + "/",
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
