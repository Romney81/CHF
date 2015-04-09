function windowH() {
    var wH = $(window).height();
    $('.hero').css({height: wH});
}
windowH();

$(window).on('scroll',function(){

    var mainbottom = $(window).height();

    // we round here to reduce a little workload
    stop = Math.round($(window).scrollTop());
    if (stop > mainbottom) {
        $('.navbar-top').addClass('past-hero', 1000);
        $('.nav-logo').hide();
        $('.nav-logo-dark').show();
    } else {
        $('.navbar-top').removeClass('past-hero');
        $('.nav-logo').show();
        $('.nav-logo-dark').hide();
   }

});
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
