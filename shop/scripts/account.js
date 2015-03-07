$(function() {

    $('.editaccount').on('click', function() {
        event.preventDefault();

        $.loadmodal({
            url: "/shop/account.edit/",
            title: "Edit User Information",
            width: "60%",

        });
    });

    $('#user_edit').ajaxForm(function(data) {
        $('#jquery-loadmodal-js-body').html(data);
    });


    $('.changepassword').on('click', function() {
        event.preventDefault();

        $.loadmodal({
            url: "/shop/account.changepassword/",
            title: "Change User Password",
            width: "40%",

        });
    });

    $('#user_changepassword').ajaxForm(function(data) {
        $('#jquery-loadmodal-js-body').html(data);
    });

});
