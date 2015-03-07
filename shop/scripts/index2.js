$(function() {
    $('.add_button').on('click', function() {

        var pid = $(this).attr('data-pid');
        var qty = 1;

        $.loadmodal({
            url: "/shop/shopping_cart.add/" + pid + "/" + qty,
            title: "Shopping Cart",

        });
    });
});
