$('.delete_button').on('click', function() {
    event.preventDefault();
    var pid = $(this).attr('data-pid');
    console.log(pid)

    $.loadmodal({
        url: "/shop/shopping_cart.delete/" + pid + "/",
        title: "Shopping Cart",
        width: "60%",

    });
});
