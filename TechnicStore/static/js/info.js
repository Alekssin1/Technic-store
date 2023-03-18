import scroll from "./scrollMouse.js"
import showSlider from "./onclichFunction.js"
import {mainOnclick} from "./onclichFunction.js"

window.onclick = function (event) {
    showSlider();
    mainOnclick();
  }

let buttonAddtoWishlist = document.querySelector("button.add-favorite")
let buttonAddtoCompare = document.querySelector("button.add-compare")
buttonAddtoWishlist.addEventListener("mouseenter", function () {
    document.getElementById("containerIcon-0-2-421").style.backgroundColor = "#d5d5d5";
    document.getElementById("add-favorite").style.color = "#fd7e14";
    document.getElementById("add-favorite").style.borderBottomColor = "#fd7e14";

});
buttonAddtoWishlist.addEventListener("mouseleave", function () {
    document.getElementById("containerIcon-0-2-421").style.backgroundColor = "#ffffff";
    document.getElementById("add-favorite").style.color = "#3B6D9A";
    document.getElementById("add-favorite").style.borderBottomColor = "#3B6D9A";
});

buttonAddtoCompare.addEventListener("mouseenter", function () {
    document.getElementById("containerIcon-0-2-422").style.backgroundColor = "#d5d5d5";
    document.getElementById("add-compare").style.color = "#fd7e14";
    document.getElementById("add-compare").style.borderBottomColor = "#fd7e14";
    document.getElementById("add-compare1").style.color = "#fd7e14";
    document.getElementById("add-compare1").style.borderBottomColor = "#fd7e14";

});
buttonAddtoCompare.addEventListener("mouseleave", function () {
    document.getElementById("containerIcon-0-2-422").style.backgroundColor = "#ffffff";
    document.getElementById("add-compare").style.color = "#3B6D9A";
    document.getElementById("add-compare").style.borderBottomColor = "#3B6D9A";
    document.getElementById("add-compare1").style.color = "#3B6D9A";
    document.getElementById("add-compare1").style.borderBottomColor = "#3B6D9A";
});

$('.info').hover(
    function () {
        let top = $(this).offset().top;
        let left = $(this).offset().left - 400;
        let data = $(this).data('modal-text');

        let div = document.createElement('div');
        div.id = 'modal';
        $(div).css('top', top);
        $(div).css('left', left);
        $(div).html(data);
        $('body').append(div);
    },
    function () {
        $('#modal').remove();
    });

window.onload = scroll(".tabs-0-2-366");
window.onload = scroll(".navigation_links");

