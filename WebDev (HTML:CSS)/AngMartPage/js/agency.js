/*!
 * Start Bootstrap - Agency Bootstrap Theme (http://startbootstrap.com)
 * Code licensed under the Apache License v2.0.
 * For details, see http://www.apache.org/licenses/LICENSE-2.0.
 */

// jQuery for page scrolling feature - requires jQuery Easing plugin
$(function() {
    $('a.page-scroll').bind('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top
        }, 1500, 'easeInOutExpo');
        event.preventDefault();
    });
});

// Highlight the top nav as scrolling occurs
$('body').scrollspy({
    target: '.navbar-fixed-top'
})

// Closes the Responsive Menu on Menu Item Click
$('.navbar-collapse ul li a').click(function() {
    $('.navbar-toggle:visible').click();
});
/*
function showHemp() {
    document.getElementById("myDropdown").classList.toggle("show");
   
}

window.onclick = function (event) {
    if(!event.target.matches('dropbtn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdown[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}
*/
$(document).ready(function(){
  $('.slider1').bxSlider({
      mode: 'horizontal',
      auto: true,
      randomStart: true,
      easing: 'ease-in-out',
      speed: 1000,
      oneToOneTouch: true
  });
      /*
      onSlideNext: function(){
          $('#butters').animate({
              backgroundColor: "#999999"
          }, 4000);
      }
      */
    $('.slider2').bxSlider({
      mode: 'horizontal',
      auto: true,
      randomStart: true,
      easing: 'ease-in-out',
      speed: 1500,
      oneToOneTouch: true
  });
  
  
  
});