// hide image button (button1)

$(document).ready(function(){
  $('.button1').click(function(){
    $('.img1').hide();
    $('.img2').css({'grid-column' : '1/span 1', 'margin' : '0 auto'});
  })
}); 

// toggle show image button (button2)