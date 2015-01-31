$(function() {
  // update the time every n seconds
  window.setInterval(function() {
    $('.browser-time').text('The current browser time is ' + new Date());
  }, ${ request.urlparams[1] if request.urlparams[1] else 500 });

	// update button
	$('#server-time-button').click(function() {
	  $('.server-time').load('/homepage/index.gettime');
	});
});

    
/*Menu-toggle*/
$("#menu-toggle").click(function(e) {
    e.preventDefault();
    $("#wrapper").toggleClass("active");
});

/*Scroll Spy*/
$('body').scrollspy({ target: '#spy', offset:80});

/*Smooth link animation*/
$('a[href*=#]:not([href=#])').click(function() {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') || location.hostname == this.hostname) {

        var target = $(this.hash);
        target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
        if (target.length) {
            $('html,body').animate({
                scrollTop: target.offset().top
            }, 1000);
            return false;
        }
    }
});