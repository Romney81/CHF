$(function() {
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
});
