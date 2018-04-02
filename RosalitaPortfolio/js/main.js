// about page image hover

$(document).ready(function() {
	$('.preview').on('mouseover focus', function() {
		$('.psst').text($(this).attr('alt'));
		$('.psst').css('background-image', 'url("'+ $(this).attr('src')+ '")');
	$('.preview').on('mouseleave blur', function() {
		$('.psst').text("Hover over an image below!");
		$('.psst').css('background-image', '');
})
	})
})

