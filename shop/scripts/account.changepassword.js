$(function() {
    $('#user_changepassword').ajaxForm(function(data) {
        $('#jquery-loadmodal-js-body').html(data);
    });

    $('input').addClass('form-control');
});
