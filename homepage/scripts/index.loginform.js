$(function() {
    $('#loginform').ajaxForm(function(data) {
        $('#custom-modal').find('.modal-body').html(data);
    });
});
