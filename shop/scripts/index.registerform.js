$(function() {
    $('#registerform').ajaxForm(function(data) {
        $('#custom-modal').find('.modal-body').html(data);
    });
    $('input').addClass('form-control');
    $('#id_username').attr('placeholder', 'Username');
    $('#id_password1').attr('placeholder', 'Password');
    $('#id_password2').attr('placeholder', 'Password Confirmation');
});
