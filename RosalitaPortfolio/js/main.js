// about page image hover

$(document).ready(function() {
 // Wrap every .img in a div
  // 1. For all items with class .img...
  // 2. Wrap them in a div
	$(".preview").wrap('<div class="alt-wrap"/>');

	// Add alt text after each .img
  // 1. For all items with class .img...
  // 2. Run a function for each of them...
  // 3. To add a p element after it
  // 5. Containing that element's alt text
	$(".preview").each(function() {
		$(this).after('<p class="alt">' + $(this).attr('alt') + '</p>');
	})
})
// CSS shows/hides the alt text on hover









// $("memories.html").ready(function() {}
// 	$(".xmas").click(function () {
// 	    $(".layout").css("display", "block");
// 	    $(".layout").text($(this).attr('alt')); 
// 	})
// })


// $("#preview").on("click", function() {
// 	 $('.xmas').text($(this).attr("alt"));
// 	});







// $(document).ready(function() {
// 	console.log("check")
// 	$('#preview').on('mouseover', function() {
// 		$(this).text($(this).attr('alt'));
// 		$(this).css('background-image', 'url("'+ $(this).attr('src')+ '")');
// 	$('#preview').on('mouseleave', function() {
// 		$(this).text("Hover over an image below!");
// 		$(this).css('background-image', '');
// })
// 	})
// })

