$(function() {
    $('.return').on('click', function() {
        event.preventDefault();
        var rid = $(this).attr('data-rid');
        $.loadmodal({
            url: "/administrator/returns.itemreturn/" + rid,
            title: "Rental Return",
            width: "50%",
            onShow: function() {
                $('.was_returned').bootstrapSwitch({
                    'size':'small',
                    'onColor': 'success',
                    'onText': 'Returned',
                    'offText': 'Out',
                });
                $('.fee').parent().addClass('col-md-2');
            },

        });
    });
    $('#return-form').ajaxForm(function(data) {
        $('#jquery-loadmodal-js-body').html(data);
    });

});
