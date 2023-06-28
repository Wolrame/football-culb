document.addEventListener("DOMContentLoaded", function () {
	var menuLinks = document.querySelectorAll(".nav ul li a");

	// Event handler when menu item is clicked
	menuLinks.forEach(function (link) {
		link.addEventListener("click", function (e) {
			e.preventDefault(); // Prevent following the link

			var targetId = link.getAttribute("href"); // Get the href attribute
			var targetSection = document.querySelector(targetId); // Get section by ID

			// Smooth scrolling to section
			window.scrollTo({
				top: targetSection.offsetTop,
				behavior: "smooth"
			});
		});
	});
});
