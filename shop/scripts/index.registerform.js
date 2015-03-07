$(function() {
    $('#registerform').ajaxForm(function(data) {
        $('#custom-modal').find('.modal-body').html(data);
    });
});
