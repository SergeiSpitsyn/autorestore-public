jQuery(document).ready(function($) {
   "use strict";

    //  HEADER SLIDER HOOK
   jQuery('#index-slider2').fadeIn(1000);
   $('#index-slider2').sliderPro({
   width: 955,
   height: 610,
   visibleSize: '100%',
   forceSize: 'fullWidth',
   arrows: true,
   autoplay: true,
   autoplayDelay: 8500,
   autoplayOnHover: 'none',
   slideDistance: 0,
   breakpoints: {
     1025: {
          width: '75%'
     },
     500: {
         width: '100%',
         arrows: false
     }
 }
});
     //  TESTIMONIALS CAROUSEL HOOK
     $('#customers-testimonials').owlCarousel({
       loop: true,
       items: 1,
       margin: 0,
       autoplay: true,
       autoplayTimeout: 8500,
       animateIn: 'fadeIn',
       animateOut: 'rotateOutUpRight',
       lazyLoad: true,
     });
     //  CLIENTS CAROUSEL HOOK
     $('#clients-carousel').owlCarousel({
       loop: true,
       items: 5,
       margin: 30,
       autoplay: true,
       autoplayTimeout: 8500,
       smartSpeed: 450,
       responsive: {
         0: {
           items: 2
         },
         768: {
           items: 3
         },
         1170: {
           items: 5
         }
       }
     });

});

$('.lightbox').magnificPopup({
   type: 'image',
   gallery:{
     enabled:true
   },
   retina: {
     ratio: 1,
     replaceSrc: function(item, ratio) {
       return item.src.replace(/.w+$/, function(m) { return '@2x' + m; });
 } // function that changes image source
}
});