$(function() {
    $('#thirty').DataTable({
        responsive: true,
        retrieve: true,
    });
    $('#sixty').DataTable({
        responsive: true,
        retrieve: true,
    });
    $('#ninety').DataTable({
        responsive: true,
        retrieve: true,
    });

    // ajax call for emails.
    $('.btn-email').on('click', function() {
        event.preventDefault();
        var email = $(this).attr('data-email');
        $.ajax({
            url: '/administrator/overdue.sendmail/' + email,
            success: function(data) {
                $.notify({
                    message: 'Your Emails Have Been Sent',
                    icon: 'fa fa-check',
                }, {
                    type: 'success',
                    animate: {
                        enter: 'animated fadeInDown',
                        exit: 'animated fadeOutUp'
                    },
                });
            },
        })

    });

});
