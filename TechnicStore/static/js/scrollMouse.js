// window.onload = scroll(".tabs-0-2-366");



export default function scroll(className) {
    var scr = $(className);
    scr.mousedown(function () {
        var startX = this.scrollLeft + event.pageX;
        scr.mousemove(function () {
            this.scrollLeft = startX - event.pageX;
            return false;
        });
    });

    $(window).mouseup(function () {
        scr.off("mousemove");
    });
}