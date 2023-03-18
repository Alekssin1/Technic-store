$(document).ready(function(){   
    BinHide(false);
});

function BinShow(){
    var inp = document.getElementById("bin");
    inp.style.opacity = '1';
    document.getElementById("bin").style.transition = "opacity .3s cubic-bezier(0, 0, 1, 1), visibility .3s";
    document.getElementById("bin").style.visibility = "inherit";
    document.getElementById("bin").style.zIndex = 200;
    $("body").css("overflow","hidden"); 
}

function BinHide(second=true){
    var inp = document.getElementById("bin");
    if (second) {
       document.getElementById("bin").style.transition = "opacity .3s cubic-bezier(0, 0, 1, 1), visibility .3s"; 
    }
    inp.style.opacity = '0';
    document.getElementById("bin").style.visibility = "hidden";
    document.getElementById("bin").style.zIndex = 200;
    $("body").css("overflow","auto");
}

function BinDell(){
    var inp = document.getElementById("bin");
    document.getElementById("bin").style.transition = "opacity .3s cubic-bezier(0, 0, 1, 1), visibility .3s";
    inp.style.opacity = '1';
    document.getElementById("bin").style.visibility = "inherit";
    document.getElementById("bin").style.zIndex = 200;
}

function countPlus() {
    var inp = document.getElementById("count");
    inp.textContent = parseInt(inp.textContent)+1;
}

function countMinus(id){
    var inp = document.getElementById("count");
    var my_inp = document.getElementById("number__"+id)
    inp.textContent = parseInt(inp.textContent) - my_inp.value;
}

function clickMinus(id) {
    var inp = document.getElementById("count");
    var my_inp = document.getElementById("number__"+id)
    if (my_inp.value > 1) {
        inp.textContent = parseInt(inp.textContent) - 1;
    }    
}

