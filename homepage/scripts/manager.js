$(function() {
    
    $('.header').hide();
    
    $('#side-menu').metisMenu();

    $('.ru').click(function(event) {
        event.preventDefault();
        $('.manage').hide();
        $('.manage-ru').show();
        $('#users-table').DataTable({
                responsive: true,
                retrieve: true,
        });
        event.preventDefault(); 
    });
    $('.event').click(function(event) {
        event.preventDefault();
	    $('.manage').hide();
        $('.manage-event').show(); 
        event.preventDefault();
    });
    $('.item').click(function(event) {
        event.preventDefault();
	    $('.manage').hide();
        $('.manage-item').show();
        $('#items-table').DataTable({
                responsive: true,
                retrieve: true,
        }); 
        event.preventDefault();
    });
    $('.product').click(function(event) {
        event.preventDefault();
	    $('.manage').hide();
        $('.manage-product').show(); 
        $('#products-table').DataTable({
                responsive: true,
                retrieve: true,
        });
        event.preventDefault();
    });

});



//Loads the correct sidebar on window load,
//collapses the sidebar on window resize.
// Sets the min-height of #page-wrapper to window size
$(function() {
    $(window).bind("load resize", function() {
        topOffset = 50;
        width = (this.window.innerWidth > 0) ? this.window.innerWidth : this.screen.width;
        if (width < 768) {
            $('div.navbar-collapse').addClass('collapse');
            topOffset = 100; // 2-row-menu
        } else {
            $('div.navbar-collapse').removeClass('collapse');
        }

        height = ((this.window.innerHeight > 0) ? this.window.innerHeight : this.screen.height) - 1;
        height = height - topOffset;
        if (height < 1) height = 1;
        if (height > topOffset) {
            $("#page-wrapper").css("min-height", (height) + "px");
        }
    });

    var url = window.location;
    var element = $('ul.nav a').filter(function() {
        return this.href == url || url.href.indexOf(this.href) == 0;
    }).addClass('active').parent().parent().addClass('in').parent();
    if (element.is('li')) {
        element.addClass('active');
    }
});
