// hide image button (button1)

$(document).ready(function(){
  $('.button1').click(function(){
    $('.img1').hide();
    $('.wrapper').css('grid-template-columns', 'auto')
    $('.img2').css({'grid-column' : '1/span 1', 'margin' : '0 auto'});
  })

  $('.button2').click(function(){
  	$('.img1').show();
  	$('.wrapper').css('grid-template-columns', 'auto auto')
  	$('.img2').css({'grid-column' : '2/span 1'});
  })
}); 

// show image button (button2)