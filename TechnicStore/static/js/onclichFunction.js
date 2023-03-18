export function mainOnclick() {
    if (event.target.matches('.login')) {
        document.getElementById("login").style.display = "none";
        document.getElementById("register__menu").style.display = "none";
        document.getElementById("login__menu").style.display = "none";
        document.body.style.overflow = 'auto';
        document.getElementById("register__menu").classList.remove("register__menu-active");
        document.getElementById("login__menu").classList.remove("login__menu-active");

    }

    if (event.target.matches('.left__menu')) {
        document.getElementById("myDropdown__mobile").style.display = "none";
        document.body.style.overflow = 'auto';
    }

    if (event.target.matches('.catalog__mobile') || event.target.matches('.catalog__mobile img[alt="exit"]')) {
        document.getElementById("catalog__mobile").style.display = "none";
        document.getElementById("catalog__mobile__all").classList.remove("catalog__mobile__all-active");
    }
}

export function catalogOnclick() {
    if (document.getElementById("sorting__list").style.display === "block" && !event.target.matches('.sorting__list')
        && !event.target.matches('.sorting__list ul') && !event.target.matches('.sorting__list ul a') &&
        !event.target.matches('.sorting__list ul a li')) {
        document.getElementById("sorting__list").style.display = "none";
        document.getElementById('sorting__svg').style.transform = "rotate(0)";
    }

    else if (event.target.matches('.sorting__filter p') || event.target.matches('.sorting__menu .sorting__svg')) {
        document.getElementById("sorting__list").style.display = "block";
        document.getElementById('sorting__svg').style.transform = "rotate(180deg)";
    }

    if (event.target.matches('.catalog__palce') || event.target.matches('.catalog__palce svg')
        || event.target.matches('.catalog__palce div') || event.target.matches('.catalog__palce h4')) {
        document.getElementById("catalog__page__catalog__page__background").classList.add("catalog__page__background");
        document.getElementById("catalog__filter").style.display = "block";
    }

    if (event.target.matches('.catalog__page__background')) {
        document.getElementById("catalog__page__catalog__page__background").classList.remove("catalog__page__background");
        document.getElementById("catalog__filter").style.display = "none";
    }
}

export function sortingOnclick() {
    if (document.getElementById("comparison__sorting").style.display === "block" &&
        !event.target.matches('.comparison__sorting') && !event.target.matches('.comparison__sorting ul') &&
        !event.target.matches('.comparison__sorting a') && !event.target.matches('.comparison__sorting li')) {
        document.getElementById("comparison__sorting").style.display = "none";
    }
    else if (event.target.matches('.comparison__choice') || event.target.matches('.comparison__svg')) {
        document.getElementById("comparison__sorting").style.display = "block";
    }
}

export default function showSlider() {
    if (event.target.matches('.showMore')) {
        document.body.style.overflow = 'hidden';
        document.getElementById("showMoreSlider").style.zIndex = 401;
        document.getElementById("showMoreSlider").style.opacity = 1;
    }

    if(event.target.matches('.ShowMoreSVG') || event.target.matches('.ShowMoreSVG path')) {
        document.body.style.overflow = 'auto';
        document.getElementById("showMoreSlider").style.zIndex = -1;
        document.getElementById("showMoreSlider").style.opacity = 0;
    }
}