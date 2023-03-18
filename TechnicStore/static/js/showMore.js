showMore('.checkbox__brands .hidden', '.checkbox__brands div.box', 'show__more__mobile', 'close__mobile',
    'more__SVG__mobile', '.brands__mobile');
showMore('.checkbox__builtIn__memoryMobile .hidden', '.checkbox__builtIn__memoryMobile div.box', 'show__more__builtIn__memoryMobile',
    'close__builtIn__memoryMobile', 'more__SVG__builtIn__memoryMobile', '.builtIn__memoryMobile');
showMore('.checkbox__RAMmobile .hidden', '.checkbox__RAMmobile div.box', 'show__more__RAMmobile', 'close__RAMmobile',
    'more__SVG__RAMmobile', '.RAMmobile');
showMore('.checkbox__screenType__mobile .hidden', '.checkbox__screenType__mobile div.box', 'show__more__screenType__mobile',
    'close__screenType__mobile', 'more__SVG__screenType__mobile', '.screenType__mobile');
showMore('.checkbox__mobile__processor .hidden', '.checkbox__mobile__processor div.box', 'show__more__mobile__processor',
    'close__mobile__processor', 'more__SVG__mobile__processor', '.mobile__processor');
showMore('.checkbox__screen__resolution .hidden', '.checkbox__screen__resolution div.box', 'show__more__screen__resolution',
    'close__screen__resolution', 'more__SVG__screen__resolution', '.screen__resolution');


closeTitle("price__filter__title", "price__filter__content", "price__filter__svg");
closeTitle("brands__filter__title", "brands__filter__content", "brands__filter__svg");
closeTitle("memoryMobile__filter__title", "memoryMobile__filter__content", "memoryMobile__filter__svg");
closeTitle("RAMmobile__filter__title", "RAMmobile__filter__content", "RAMmobile__filter__svg");
closeTitle("screenType__mobile__filter__title", "screenType__mobile__filter__content", "screenType__mobile__filter__svg");
closeTitle("main__camera__filter__title", "main__camera__filter__content", "main__camera__filter__svg");
closeTitle("front__camera__filter__title", "front__camera__filter__content", "front__camera__filter__svg");
closeTitle("battery__filter__title", "battery__filter__content", "battery__filter__svg");
closeTitle("mobile__processor__filter__title", "mobile__processor__filter__content", "mobile__processor__filter__svg");
closeTitle("blocking__filter__title", "blocking__filter__content", "blocking__filter__svg");
closeTitle("NFC__filter__title", "NFC__filter__content", "NFC__filter__svg");
closeTitle("protectionWater__filter__title", "protectionWater__filter__content", "protectionWater__filter__svg");
closeTitle("screen__resolution__filter__title", "screen__resolution__filter__content", "screen__resolution__filter__svg");
closeTitle("screen__size__filter__title", "screen__size__filter__content", "screen__size__filter__svg");
closeTitle("5G__filter__title", "5G__filter__content", "5G__filter__svg");
closeTitle("stereo__speakers__filter__title", "stereo__speakers__filter__content", "stereo__speakers__filter__svg");
closeTitle("number__cameras__filter__title", "number__cameras__filter__content", "number__cameras__filter__svg");
closeTitle("bluetooth__filter__title", "bluetooth__filter__content", "bluetooth__filter__svg");
closeTitle("wireless__charger__filter__title", "wireless__charger__filter__content", "wireless__charger__filter__svg");
closeTitle("fast__charging__filter__title", "fast__charging__filter__content", "fast__charging__filter__svg");


function showMore(hidenBlock, unhiddenBlock, open, close, more__SVG, mostObject) {
    var more = document.querySelectorAll(mostObject);
    var show__more = document.getElementById(open);
    var closer = document.getElementById(close);
    var svgElement = document.getElementById(more__SVG);

    for (var i = 0; i < more.length; i++) {
        more[i].addEventListener('click', function () {
            var hidden = this.parentNode.querySelectorAll(hidenBlock);
            var unhidden = this.parentNode.querySelectorAll(unhiddenBlock);

            var showPerClick = hidden.length;
            var hideClich = unhidden.length;

            if (hideClich) {
                show__more.style.display = "block";
                closer.style.display = "none";
                svgElement.style.transform = "rotate(0)";
                for (var i = 0; i < hideClich; i++) {
                    unhidden[i].classList.add('hidden');
                    unhidden[i].classList.remove('box');
                }
            }
            else {
                show__more.style.display = "none";
                closer.style.display = "block";
                svgElement.style.transform = "rotate(180deg)";
                for (var i = 0; i < showPerClick; i++) {
                    if (!hidden[i]) return this.outerHTML = "";
                    hidden[i].classList.add('box');
                    hidden[i].classList.remove('hidden');
                }
            }
        });
    }
}

function closeTitle(titleId, condentId, svgImage) {
    var title = document.getElementById(titleId);
    var content = document.getElementById(condentId);
    var thisSvg = document.getElementById(svgImage);


    title.addEventListener('click', function () {
        content.classList.toggle("poshelNa");
        thisSvg.style.transform === "rotate(180deg)" ? thisSvg.style.transform = "rotate(0)" : thisSvg.style.transform = "rotate(180deg)";
    });
}
