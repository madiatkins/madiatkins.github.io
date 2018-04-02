$(document).ready(function() {
	$('.preview').on('mouseover focus', function() {
		$('#image').text($(this).attr('alt'));
		$('#image').css('background-image', 'url("'+ $(this).attr('src')+ '")');
	$('.preview').on('mouseleave blur', function() {
		$('#image').text("Hover over an image below!");
		$('#image').css('background-image', '');
})
	})
})

