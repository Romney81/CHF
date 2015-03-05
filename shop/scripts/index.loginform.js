$(function() {
    $('#loginform').ajaxForm(function(data) {
        $('#login-modal').find('.modal-body').html(data);
    });
});
