$(function() {
    $('#login-modal').modal({
            show:false,
    });

    $('#login-modal-button').on('click', function() {
        event.preventDefault();
        $('#login-modal').modal('show');
        $.ajax({
            url: '/shop/index.loginform',
            success: function (data) {
                $('#login-modal').find('.modal-body').html(data);
            },

        });
    });
});
