import { mainOnclick } from "./onclichFunction.js";
import scroll from "./scrollMouse.js"

window.onclick = function (event) {
  mainOnclick();
}

window.onload = scroll(".brands");