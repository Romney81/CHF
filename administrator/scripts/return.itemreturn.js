$(function() {
    $('#return-form').ajaxForm(function(data) {
        $('#jquery-loadmodal-js-body').html(data);
    });
});
