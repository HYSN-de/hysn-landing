(function ($) {
	"use strict";

	$(window).on('load', function () {
		preloader();
		wowAnimation();
	});

	/*------------------------------------------
	= preloader
	-------------------------------------------*/
	function preloader() {
		$('#preloader').fadeOut('slow',function(){
			$(this).remove();
		});
	}

	// gsap
	gsap.config({
		nullTargetWarn: false,
	});
	
	/*------------------------------------------
	= back to top
	-------------------------------------------*/
	$(window).scroll(function () {
		if ($(this).scrollTop() > 500) {
			$('.xb-backtotop').addClass('active');
		} else {
			$('.xb-backtotop').removeClass('active');
		}
	});  
	$(function () {
		$(".scroll").on('click', function () {
			$("html,body").animate({ scrollTop: 0 }, "slow");
			return false
		});
	});

	/*------------------------------------------
	= sticky header
	-------------------------------------------*/
	function stickyHeader() {
		var scrollDirection = "";
		var lastScrollPosition = 0;

		// Clone and make header sticky if the element with class 'xb-header' exists
		if ($('.xb-header').length) {
			$('.xb-header').addClass('original').clone(true).insertAfter('.xb-header').addClass('xb-header-area-sticky xb-sticky-stt').removeClass('original');
		}

		// Handle scroll events
		$(window).on("scroll", function () {
			var currentScrollPosition = $(window).scrollTop();

			// Determine scroll direction
			scrollDirection = currentScrollPosition < lastScrollPosition ? "up" : "down";
			lastScrollPosition = currentScrollPosition;

			// Check if element with ID 'xb-header-area' has class 'is-sticky'
			if ($("#xb-header-area").hasClass("is-sticky")) {
				// Add or remove classes based on scroll position for sticky header and mobile header
				if (lastScrollPosition > 100) {
					$(".xb-header-area-sticky.xb-sticky-stb").addClass("xb-header-fixed");
				} else {
					$(".xb-header-area-sticky.xb-sticky-stb").removeClass("xb-header-fixed");
				}

				// Add or remove classes for sticky header based on scroll direction
				if (scrollDirection === "up" && lastScrollPosition > 100) {
					$(".xb-header-area-sticky.xb-sticky-stt").addClass("xb-header-fixed");
				} else {
					$(".xb-header-area-sticky.xb-sticky-stt").removeClass("xb-header-fixed");
				}
			}
		});
	}
	stickyHeader();

	/*------------------------------------------
	= header search
	-------------------------------------------*/
	$(".header-search-btn").on("click", function (e) {
		e.preventDefault();
		$(".header-search-form-wrapper").addClass("open");
		$('.header-search-form-wrapper input[type="search"]').focus();
		$('.body-overlay').addClass('active');
	});
	$(".xb-search-close").on("click", function (e) {
		e.preventDefault();
		$(".header-search-form-wrapper").removeClass("open");
		$("body").removeClass("active");
		$('.body-overlay').removeClass('active');
	});

	/*------------------------------------------
	= sidebar
	-------------------------------------------*/
	$('.sidebar-menu-close, .body-overlay').on('click', function () {
		$('.offcanvas-sidebar').removeClass('active');
		$('.body-overlay').removeClass('active');
	});

	$('.offcanvas-sidebar-btn').on('click', function () {
		$('.offcanvas-sidebar').addClass('active');
		$('.body-overlay').addClass('active');
	});
	$('.body-overlay').on('click', function () {
		$(this).removeClass('active');
		$(".header-search-form-wrapper").removeClass("open");
	});


	/*------------------------------------------
	= mobile menu
	-------------------------------------------*/
	$('.xb-nav-hidden li.menu-item-has-children > a').append('<span class="xb-menu-toggle"></span>');
	$('.xb-header-menu li.menu-item-has-children, .xb-menu-primary li.menu-item-has-children').append('<span class="xb-menu-toggle"></span>');
	$('.xb-menu-toggle').on('click', function () {
		if (!$(this).hasClass('active')) {
			$(this).closest('ul').find('.xb-menu-toggle.active').toggleClass('active');
			$(this).closest('ul').find('.sub-menu.active').toggleClass('active').slideToggle();
		}
		$(this).toggleClass('active');
		$(this).closest('.menu-item').find('> .sub-menu').toggleClass('active');
		$(this).closest('.menu-item').find('> .sub-menu').slideToggle();
	});

	$('.xb-nav-hidden li.menu-item-has-children > a').click(function (e) {
		var target = $(e.target);
		if ($(this).attr('href') === '#' && !(target.is('.xb-menu-toggle'))) {
			e.stopPropagation();
			if (!$(this).find('.xb-menu-toggle').hasClass('active')) {
				$(this).closest('ul').find('.xb-menu-toggle.active').toggleClass('active');
				$(this).closest('ul').find('.sub-menu.active').toggleClass('active').slideToggle();
			}
			$(this).find('.xb-menu-toggle').toggleClass('active');
			$(this).closest('.menu-item').find('> .sub-menu').toggleClass('active');
			$(this).closest('.menu-item').find('> .sub-menu').slideToggle();
		}
	});
	$(".xb-nav-mobile").on('click', function () {
		$(this).toggleClass('active');
		$('.xb-header-menu').toggleClass('active');
	});

	$(".xb-menu-close, .xb-header-menu-backdrop").on('click', function () {
		$(this).removeClass('active');
		$('.xb-header-menu').removeClass('active');
	});

	/*------------------------------------------
	= nice select
	-------------------------------------------*/
	$('select').niceSelect();

	/*------------------------------------------
	= data background and bg color
	-------------------------------------------*/
	$("[data-background]").each(function () {
		$(this).css("background-image", "url(" + $(this).attr("data-background") + ") ")
	})
	$("[data-bg-color]").each(function () {
		$(this).css("background-color", $(this).attr("data-bg-color"));

	});

	/*------------------------------------------
	= aos animation
	-------------------------------------------*/
	function wowAnimation() {
		var wow = new WOW({
			boxClass: 'wow',
			animateClass: 'animated',
			offset: 0,
			mobile: false,
			live: true
		});
		wow.init();
	}

	/*------------------------------------------
	= counter
	-------------------------------------------*/
	if ($(".xbo").length) {
		$('.xbo').appear();
		$(document.body).on('appear', '.xbo', function (e) {
			var odo = $(".xbo");
			odo.each(function () {
				var countNumber = $(this).attr("data-count");
				$(this).html(countNumber);
			});
			window.xboOptions = {
				format: 'd',
			};
		});
	}

	if ($(".xbo_trigger").length) {
        var odo = $(".xbo_trigger");
        odo.each(function () {
            var countNumber = $(this).attr("data-count");
            var odometerInstance = new Odometer({
                el: this,
                value: 0,
                format: 'd',
            });
            odometerInstance.render();
            odometerInstance.update(countNumber);
        });
        $('.xbo_trigger').appear();
        $(document.body).on('appear', '.xboh', function (e) {
            // This event handler can be empty or used for additional functionality if needed
        });
    }

	/*------------------------------------------
	= smooth scroll
	-------------------------------------------*/
	const lenis = new Lenis({
		duration: .8,
		smoothWheel: true,
	});

	function raf(time) {
		lenis.raf(time);
		requestAnimationFrame(raf);
	}
	requestAnimationFrame(raf);

	/*------------------------------------------
	= isotop
	-------------------------------------------*/
	$('.grid').imagesLoaded(function () {
		var $grid = $('.grid').isotope({
			itemSelector: '.grid-item',
			percentPosition: true,
			masonry: {
				// use outer width of grid-sizer for columnWidth
				columnWidth: '.grid-item',
			}
		});

		// filter items on button click
		$('.xb-project-menu').on('click', 'button', function () {
			var filterValue = $(this).attr('data-filter');
			$grid.isotope({ filter: filterValue });
		});
	});

	//for menu active class
	$('.xb-project-menu button').on('click', function (event) {
		$(this).siblings('.active').removeClass('active');
		$(this).addClass('active');
		event.preventDefault();
	});

	
	
	/*------------------------------------------
	= Text reveal With Scroll 
	-------------------------------------------*/
	if ($('.xb-text-reveal').length) {
		document.fonts.ready.then(function() {
			var textheading = $(".xb-text-reveal");
			if (textheading.length == 0) return;

			gsap.registerPlugin(SplitText);

			textheading.each(function(index, el) {
				el.split = new SplitText(el, { 
					type: "lines,words,chars",
					linesClass: "split-line"
				});

				if ($(el).hasClass('xb-text-reveal')) {
					gsap.set(el.split.chars, {
						opacity: 0.3,
						x: "-7",
					});
				}

				el.anim = gsap.to(el.split.chars, {
					scrollTrigger: {
						trigger: el,
						start: "top 92%",
						end: "top 60%",
						markers: false,
						scrub: 1,
					},
					x: "0",
					y: "0",
					opacity: 1,
					duration: 0.7,
					stagger: 0.2,
				});
			});
		});
	}

	/*------------------------------------------
	= team slide
	-------------------------------------------*/
	var slider = new Swiper(".xb-project-slider", {
		loop: true,
		speed: 400,
		spaceBetween: 40,
		slidesPerView: 3,
		centeredSlides: true,
		autoplay: {
			enabled: true,
			delay: 6000
		},
		pagination: {
			el: ".swiper-pagination",
			type: "fraction",
		},
		navigation: {
			nextEl: ".swiper-button-next",
			prevEl: ".swiper-button-prev",
		},
		breakpoints: {
			'1600': {
				slidesPerView: 3,
			},
			'1200': {
				slidesPerView: 3,
			},
			'576': {
				slidesPerView: 1,
			},
			'0': {
				slidesPerView: 1,
			},
			
		},
	});

	/*------------------------------------------
	= testimonial slide
	-------------------------------------------*/
	var swiper = new Swiper(".xb-testimonial-author", {
		spaceBetween: 1,
		slidesPerView: 6,
		autoplay: {
			enabled: true,
			delay: 6000
		},
    });
    var swiper2 = new Swiper(".xb-testimonial-slider", {
		loop: true,
		speed: 400,
		spaceBetween: 0,
		slidesPerView: 1,
		navigation: {
			nextEl: ".swiper-button-next",
			prevEl: ".swiper-button-prev",
		},
		thumbs: {
			swiper: swiper,
		},
    });
	/*------------------------------------------
	= history slide
	-------------------------------------------*/
	var swiperHistory = new Swiper(".xb-history-year-slider", {
		spaceBetween: 0,
		slidesPerView: 8,
		direction: "vertical",
		autoplay: {
			enabled: true,
			delay: 6000
		},
    });
    var swiperHistory2 = new Swiper(".xb-history-slider", {
		loop: true,
		speed: 400,
		spaceBetween: 0,
		slidesPerView: 1,
		navigation: {
			nextEl: ".swiper-button-next",
			prevEl: ".swiper-button-prev",
		},
		thumbs: {
			swiper: swiperHistory,
		},
    });


	/*------------------------------------------
	= blog slide
	-------------------------------------------*/
	var slider = new Swiper(".blog-slider", {
		loop: true,
		speed: 400,
		spaceBetween: 10,
		slidesPerView: 1,
		centeredSlides: false,
		autoplay: {
			enabled: true,
			delay: 6000
		},
		pagination: {
			el: ".swiper-pagination",
		},
		navigation: {
			nextEl: ".swiper-button-next",
			prevEl: ".swiper-button-prev",
		},
		breakpoints: {
			'1600': {
				slidesPerView: 1,
			},
			'1024': {
				slidesPerView: 1,
			},
			'768': {
				slidesPerView: 1,
			},
			'576': {
				slidesPerView: 1,
			},
			'0': {
				slidesPerView: 1,
			},
		},
	});

	/*------------------------------------------
	= cg-project-slider
	-------------------------------------------*/
	var slider = new Swiper(".cg-project-slider", {
		loop: true,
		speed: 400,
		spaceBetween: 40,
		slidesPerView: 3,
		centeredSlides: false,
		autoplay: {
			enabled: true,
			delay: 6000
		},
		breakpoints: {
			'1600': {
				slidesPerView: 3,
			},
			'992': {
				slidesPerView: 3,
			},
			'768': {
				spaceBetween: 20,
				slidesPerView: 3,
			},
			'576': {
				slidesPerView: 1,
			},
			'0': {
				slidesPerView: 1,
			},
		},
	});

	/*------------------------------------------
	= cg-testimonial-slider
	-------------------------------------------*/
	var slider = new Swiper(".cg-testimonial-slider", {
		loop: true,
		speed: 400,
		spaceBetween: 20,
		slidesPerView: 1,
		centeredSlides: false,
		autoplay: {
			enabled: true,
			delay: 6000
		},
		pagination: {
			el: ".swiper-pagination",
			clickable: true,
		},
		breakpoints: {
			'1600': {
				slidesPerView: 1,
			},
			'576': {
				slidesPerView: 1,
			},
			'0': {
				slidesPerView: 1,
			},
		},
	});

	/*------------------------------------------
	= inhover active
	-------------------------------------------*/
	$(".xb-mouseenter").on('mouseenter', function () {
		$(".xb-mouseenter").removeClass("active");
		$(this).addClass("active");
	});
	$(".xb-mouseenter2").on('click', function () {
		$(".xb-mouseenter2").removeClass("active");
		$(this).addClass("active");
	});

	/*------------------------------------------
	= click button active
	-------------------------------------------*/
	$(function () {
		$('.category li').on('click', function () {
			var active = $('.category li.active');
			active.removeClass('active');
			$(this).addClass('active');
		});
	});

	/*------------------------------------------
	= magnificPopup
	-------------------------------------------*/
	$('.popup-image').magnificPopup({
		type: 'image',
		gallery: {
			enabled: true
		}
	});
	$('.popup-video').magnificPopup({
		type: 'iframe',
		mainClass: 'mfp-zoom-in',
	});

	/*------------------------------------------
	= Accordion Box
	-------------------------------------------*/
	if ($(".accordion_box").length) {
		$(".accordion_box").on("click", ".acc-btn", function () {
			var outerBox = $(this).parents(".accordion_box");
			var target = $(this).parents(".accordion");

			if ($(this).next(".acc_body").is(":visible")) {
				$(this).removeClass("active");
				$(this).next(".acc_body").slideUp(300);
				$(outerBox).children(".accordion").removeClass("active-block");
			} else {
				$(outerBox).find(".accordion .acc-btn").removeClass("active");
				$(this).addClass("active");
				$(outerBox).children(".accordion").removeClass("active-block");
				$(outerBox).find(".accordion").children(".acc_body").slideUp(300);
				target.addClass("active-block");
				$(this).next(".acc_body").slideDown(300);
			}
		});
	}
	
	/*------------------------------------------
	= marquee
	-------------------------------------------*/
	$('.marquee-left').marquee({
		speed: 20,
		gap: 0,
		delayBeforeStart: 0,
		direction: 'left',
		duplicated: true,
		pauseOnHover: false,
		startVisible: true,
	});	

	/*------------------------------------------
	= element parallax (button)
	-------------------------------------------*/
	$('.xb-element-parallax').each(function () {
		var $this = $(this);
		var dampingFactor = 0.5;
		function handleMouseMove(e) {
			var offset = $this.offset();
			var mouseX = e.pageX - offset.left;
			var mouseY = e.pageY - offset.top;
			var translateX = (mouseX - $this.width() / 2) * dampingFactor;
			var translateY = (mouseY - $this.height() / 2) * dampingFactor;
			var translateTransform = 'translate(' + translateX + 'px, ' + translateY + 'px)';
			$this.css({
				'transform': translateTransform,
				'transition': 'transform 0.1s ease-out'  // Adjust the duration and easing as needed
			});
		}
		function resetTransform() {
			$this.css({
				'transform': 'none',
				'transition': 'transform 0.3s ease-out'  // Adjust the duration and easing as needed
			});
		}
		if ($this.closest('.xb-parent-element-parallax').length) {
			var pare2 = $this.closest('.xb-parent-element-parallax');
			pare2.on('mousemove', function (e) {
				handleMouseMove(e);
			});
			pare2.on('mouseleave', resetTransform);
		} else {
			$this.on('mousemove', handleMouseMove);
			$this.on('mouseleave', resetTransform);
		}
	});

	/*------------------------------------------
	= Progress bar Active
	-------------------------------------------*/
	document.addEventListener("DOMContentLoaded", function() {
		const progressBars = document.querySelectorAll('.progress-bar');

		const observer = new IntersectionObserver(entries => {
			entries.forEach(entry => {
			if (entry.isIntersecting) {
				const bar = entry.target;
				const percent = bar.getAttribute('data-percent');
				bar.style.width = percent + '%';
				observer.unobserve(bar); 
			}
			});
		}, { threshold: 0.5 });

		progressBars.forEach(bar => {
			
			bar.style.width = '15%';
			
			observer.observe(bar);
		});
	});
	
	/*------------------------------------------
    = TOUCHSPIN FOR PRODUCT SINGLE PAGE
    -------------------------------------------*/
	if ($("input.product-count").length) {
		$("input.product-count").TouchSpin({
			min: 1,
			max: 1000,
			step: 1,
			buttondown_class: "btn btn-link",
			buttonup_class: "btn btn-link",
		});
	} 

	/*------------------------------------------
    = woocommerce
    -------------------------------------------*/
    if($(".checkout-section").length) {
        var showLogInBtn = $(".xb-cupon-info > a");
        var showCouponBtn = $(".showcoupon");
        var shipDifferentAddressBtn = $("#ship-to-different-address");
        var loginForm = $("form.login");
        var couponForm = $(".xb-checkout-coupon");
        var shippingAddress = $(".shipping_address");

        loginForm.hide();
        couponForm.hide();
        shippingAddress.hide();

        showLogInBtn.on("click", function(event) {
            event.preventDefault();
            loginForm.slideToggle();
            event.stopPropagation();
        });

        showCouponBtn.on("click", function(event2) {
            event2.preventDefault();
            couponForm.slideToggle();
            event2.stopPropagation();
        })

        shipDifferentAddressBtn.on("click", function(event3) {
            shippingAddress.slideToggle();
            event3.stopPropagation();
        })
    }

	/*------------------------------------------
    = hero text gsap animation
    -------------------------------------------*/
	gsap.to(".hero-one .xb_hero_big_text", {
		x: 100,
		duration: 2,
		ease: "power2.out",
		scrollTrigger: {
			trigger: ".hero-one",
			scroller: "body",
			start: "top 0%",
			end: "bottom top",
			scrub: true,  
		}
	});

	/*------------------------------------------
	= scroll stricky animation
	-------------------------------------------*/
	if (window.innerWidth >= 992) {

		const cards = document.querySelectorAll('.sticky-card');

		cards.forEach((item, index) => {
			if (index === cards.length - 1) return;

			gsap.to(item, {
				scale: 0.95,
				opacity: 0.9,
				duration: 0.8,
				ease: "power2.out",
				scrollTrigger: {
					trigger: item,
					start: 'top 12%',
					end: 'bottom 12%',
					scrub: 1,
				}
			});
		});

	}
	/*------------------------------------------
	= image scaleX animation
	-------------------------------------------*/
	if (window.innerWidth >= 992) {
		document.querySelectorAll('.xb-service-img').forEach(item => {
			gsap.from(item, {
				width: 300,
				duration: 2,
				ease: "power2.out",
				scrollTrigger: {
					trigger: item,
					start: 'top 80%',
					end: 'bottom 0%',
					scrub: 1,
				}
			});
		});
	}

	/*------------------------------------------
	= price Toggle button
	-------------------------------------------*/
	function priceToggle() {
		const monthly = document.getElementById('pills-home-tab');
		const yearly  = document.getElementById('pills-profile-tab');
		const box     = document.querySelector('.xb-pricing-nav');

		if(!monthly || !yearly || !box) return;

		yearly.addEventListener('click', () => box.classList.add('is-active'));
		monthly.addEventListener('click', () => box.classList.remove('is-active'));
	}

	document.addEventListener("DOMContentLoaded", priceToggle);
	
	
	/*------------------------------------------
	= scrollY - active 
	-------------------------------------------*/
	document.addEventListener("DOMContentLoaded", function () {

		const sections = document.querySelectorAll(".project-details-right > div[id]");
		const menuLinks = document.querySelectorAll(".xb-project-menu-item a");

		function onScroll() {
			const scrollPos = window.scrollY + 120; 

			sections.forEach(section => {
				const top = section.offsetTop;
				const height = section.offsetHeight;

				if (scrollPos >= top && scrollPos < top + height) {

					menuLinks.forEach(link => link.classList.remove("active"));

					const targetLink = document.querySelector(
						`.xb-project-menu-item a[href="#${section.id}"]`
					);

					if (targetLink) {
						targetLink.classList.add("active");
					}
				}
			});
		}

		window.addEventListener("scroll", onScroll);
		onScroll();
	});


})(jQuery);
