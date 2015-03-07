$(function() {
    $('#user_edit').ajaxForm(function(data) {
        $('#jquery-loadmodal-js-body').html(data);
    });
});
