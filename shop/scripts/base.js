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

        });
    });

    $('.cart-modal').on('click', function() {
        event.preventDefault();
        $.loadmodal({
            url: "/shop/shopping_cart/",
            title: "Shopping Cart",

        });
    });

    $('#search_button').click(function() {

        var input = $("#search_input").val()

        console.log(input)

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
