import { sortingOnclick, mainOnclick } from "./onclichFunction.js";
import scroll from "./scrollMouse.js"

window.onclick = function () {
    sortingOnclick();
    mainOnclick();
}

window.onload = scroll(".another__products");
