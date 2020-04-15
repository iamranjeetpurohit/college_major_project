$(document).ready(function() {
    $(window).scroll(function() {
        let position = $(this).scrollTop();
        // console.log(position);
        if (document.URL == "http://127.0.0.1:8000/") {
            if (position >= 50) {
                if (position >= 0 && position <= 509) {
                    $(".home").addClass("nav-active");
                    $(".mission").removeClass("nav-active");
                    $(".departments").removeClass("nav-active");
                    $(".registration").removeClass("nav-active");
                    $(".facilities").removeClass("nav-active");
                    $(".notice").removeClass("nav-active");
                    $(".location").removeClass("nav-active");
                    $(".feedback").removeClass("nav-active");
                }
                if (position >= 510 && position <= 1444) {
                    $(".home").removeClass("nav-active");
                    $(".mission").addClass("nav-active");
                    $(".departments").removeClass("nav-active");
                    $(".registration").removeClass("nav-active");
                    $(".facilities").removeClass("nav-active");
                    $(".notice").removeClass("nav-active");
                    $(".location").removeClass("nav-active");
                    $(".feedback").removeClass("nav-active");
                }
                if (position >= 1445 && position <= 2149) {
                    $(".home").removeClass("nav-active");
                    $(".mission").removeClass("nav-active");
                    $(".departments").addClass("nav-active");
                    $(".registration").removeClass("nav-active");
                    $(".facilities").removeClass("nav-active");
                    $(".notice").removeClass("nav-active");
                    $(".location").removeClass("nav-active");
                    $(".feedback").removeClass("nav-active");
                }
                if (position >= 2150 && position <= 2699) {
                    $(".home").removeClass("nav-active");
                    $(".mission").removeClass("nav-active");
                    $(".departments").removeClass("nav-active");
                    $(".registration").addClass("nav-active");
                    $(".facilities").removeClass("nav-active");
                    $(".notice").removeClass("nav-active");
                    $(".location").removeClass("nav-active");
                    $(".feedback").removeClass("nav-active");
                }
                if (position >= 2700 && position <= 3399) {
                    $(".home").removeClass("nav-active");
                    $(".mission").removeClass("nav-active");
                    $(".departments").removeClass("nav-active");
                    $(".registration").removeClass("nav-active");
                    $(".facilities").addClass("nav-active");
                    $(".notice").removeClass("nav-active");
                    $(".location").removeClass("nav-active");
                    $(".feedback").removeClass("nav-active");
                }
                if (position >= 3400 && position <= 3875) {
                    $(".home").removeClass("nav-active");
                    $(".mission").removeClass("nav-active");
                    $(".departments").removeClass("nav-active");
                    $(".registration").removeClass("nav-active");
                    $(".facilities").removeClass("nav-active");
                    $(".notice").addClass("nav-active");
                    $(".location").removeClass("nav-active");
                    $(".feedback").removeClass("nav-active");
                }
                if (position >= 3800 && position <= 4080) {
                    $(".home").removeClass("nav-active");
                    $(".mission").removeClass("nav-active");
                    $(".departments").removeClass("nav-active");
                    $(".registration").removeClass("nav-active");
                    $(".facilities").removeClass("nav-active");
                    $(".notice").removeClass("nav-active");
                    $(".location").addClass("nav-active");
                    $(".feedback").removeClass("nav-active");
                }
                if (position >= 4082) {
                    $(".home").removeClass("nav-active");
                    $(".mission").removeClass("nav-active");
                    $(".departments").removeClass("nav-active");
                    $(".registration").removeClass("nav-active");
                    $(".facilities").removeClass("nav-active");
                    $(".notice").removeClass("nav-active");
                    $(".location").removeClass("nav-active");
                    $(".feedback").addClass("nav-active");
                }
            }
        }
    });

    $(".nav-button").click(function() {
        $(".nav-button").toggleClass("change");
    });

    var value = "bsc";
    if (value === "bsc") {
        $(".filter")
            .not("." + value)
            .hide();
        $(".filter")
            .filter("." + value)
            .show();
    }
    $(".department-list-item").click(function() {
        $(this)
            .addClass("active-item")
            .siblings()
            .removeClass("active-item");
        value = $(this).attr("data-filter");
        if (value === "bsc") {
            $(".filter")
                .not("." + value)
                .hide(300);
            $(".filter")
                .filter("." + value)
                .show(300);
        } else if (value === "btech") {
            $(".filter")
                .not("." + value)
                .hide(300);
            $(".filter")
                .filter("." + value)
                .show(300);
        } else if (value === "msc") {
            $(".filter")
                .not("." + value)
                .hide(300);
            $(".filter")
                .filter("." + value)
                .show(300);
        }
    });

    $(".top").hide(0);
    $(window).scroll(function() {
        if ($(this).scrollTop() > 200) {
            $(".top").show();
        } else {
            $(".top").hide();
        }
    });

    $(".top").click(function() {
        $("html, body").animate({ scrollTop: 0 }, 600);
        return false;
    });

    $("#registration-hover").hover(function() {
        $(".registration-hover").toggleClass("hover-anim");
    });
    $("#notice-hover").hover(function() {
        $(".notice-hover").toggleClass("hover-anim");
    });
    // $(".map-hover").hover(function() {
    //     $(".featured-item").toggleClass("hover-anim");
    // });
    $("#feedback-hover").hover(function() {
        $(".feedback-hover").toggleClass("hover-anim");
    });

    //department
    $(".phy-button").hover(function() {
        $(".fa-lightbulb").toggleClass("department-icon");
    });
    $(".chem-button").hover(function() {
        $(".fa-vial").toggleClass("department-icon");
    });
    $(".maths-button").hover(function() {
        $(".fa-square-root-alt").toggleClass("department-icon");
    });
    $(".it-button").hover(function() {
        $(".fa-laptop-code").toggleClass("department-icon");
    });
    $(".mecha-button").hover(function() {
        $(".fa-cogs").toggleClass("department-icon");
    });
    $(".civil-button").hover(function() {
        $(".fa-pencil-ruler").toggleClass("department-icon");
    });
    $(".etc-button").hover(function() {
        $(".fa-microchip").toggleClass("department-icon");
    });
    $(".pei-button").hover(function() {
        $(".fa-bolt").toggleClass("department-icon");
    });


    //facility

    $("#library-slide-arrow").hover(function() {
        $(".library-slide-arrow").toggleClass("slide-arrow-right");
        // $(".fa-book-reader").toggleClass("department-icon");
    });
    $("#bus-slide-arrow").hover(function() {
        $(".bus-slide-arrow").toggleClass("slide-arrow-right");
        // $(".fa-bus").toggleClass("department-icon");
    });
    $("#hostels-slide-arrow").hover(function() {
        $(".hostels-slide-arrow").toggleClass("slide-arrow-right");
        // $(".fa-hotel").toggleClass("department-icon");
    });
    $("#internet-slide-arrow").hover(function() {
        $(".internet-slide-arrow").toggleClass("slide-arrow-right");
        // $(".fa-wifi").toggleClass("department-icon");
    });

    $("#guest-slide-arrow").hover(function() {
        $(".guest-slide-arrow").toggleClass("slide-arrow-right");
        // $(".fa-home").toggleClass("department-icon");
    });
    $("#health-slide-arrow").hover(function() {
        $(".health-slide-arrow").toggleClass("slide-arrow-right");
        // $(".fa-first-aid").toggleClass("department-icon");
    });
});
