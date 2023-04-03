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