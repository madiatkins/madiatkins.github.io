var $titles = $(".accordian__title");
var $contents = $(".accordian__content");

$titles.on("click", function() {
	// console.log('title');
	// $contents.toggle();
	var $currentTitle = $(this);
	var $currentContent = $currentTitle.next();

	$contents.slideUp() //hide, slideDown=show
	if ($currentContent.css("display") == "none"){
		$currentContent.slideToggle();
	}
	

})
