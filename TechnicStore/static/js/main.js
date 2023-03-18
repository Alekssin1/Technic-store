function showLeftMenu() {
  document.getElementById("myDropdown__mobile").style.display = "block";
  document.body.style.overflow = 'hidden';
}

function showlogin() {
  document.getElementById("login").style.display = "flex";
  document.getElementById("login__menu").style.display = "flex";
  document.body.style.overflow = 'hidden';
  setTimeout(animation, 0.1, "login__menu", "login__menu-active");
}

let buttonCatalog = document.querySelector("button.dropbtn");

buttonCatalog.addEventListener("mouseenter", function () {
  document.getElementById("myDropdown").classList.toggle("show");
  document.getElementById("header__background").classList.toggle("show");
});

function loginDisplayNone(email = "none", number = "block") {
  correct = ["block", "flex", "none"];
  if (typeof email === 'string' & typeof number === 'string' & correct.includes(email) & correct.includes(number)) {
    forEmail = Array.from(document.getElementsByClassName("login__email"));
    forNuber = Array.from(document.getElementsByClassName("login__number"));

    forEmail.forEach(element => element.style.display = email);
    forNuber.forEach(element => element.style.display = number);
  }
}

function showRegister() {
  document.getElementById("login").style.display = "flex";
  document.getElementById("register__menu").style.display = "flex";
  document.getElementById("login__menu").style.display = "none";
  setTimeout(animation, 0.1, "register__menu", "register__menu-active");
}

function closeRegister() {
  document.getElementById("register__menu").style.display = "none";
  document.getElementById("login__menu").style.display = "flex";
  setTimeout(animation, 0.1, "login__menu", "login__menu-active");
}

function showMobileCatalog() {
  document.getElementById("catalog__mobile").style.display = "flex";
  setTimeout(animation, 0.1, "catalog__mobile__all", "catalog__mobile__all-active");
}

function animation(id, toggleAtr) {
  document.getElementById(id).classList.add(toggleAtr);
}


function plusProduct(id) {
  object = document.getElementById("number__"+id);
  value = object.value;
  object_price_one = document.getElementById("product-price_"+id);
  value_price_one = object_price_one.textContent;
  value_price_one_main = value_price_one.slice(0, -1);
  value_price_one_main = Number(value_price_one_main.replace('\xa0', ''));
  value_price_one_main = value_price_one_main / value;
  value++;
  value_price_one_main = value_price_one_main * value;
  object.value = value;
  value_price_one_main = value_price_one_main.toString()
  object_price_one.textContent = value_price_one_main + " ₴";
  var elements = document.getElementsByClassName("product-price");
  sum = 0;
  for (let i = 0; i<elements.length; i++) {
    temp_value = elements[i].textContent;
    value_all = temp_value.slice(0, -1);
    value_all = Number(value_all.replace('\xa0', ''));
    sum = sum + value_all;
  }
  var total_price = document.getElementById("sum_price-number");
  total_price.textContent = sum.toString() + " ₴";
}

function minusProduct(id) {
  object = document.getElementById("number__"+id);
  value = object.value;
  
  if (!(value <= 1)) {
    object_price_one = document.getElementById("product-price_"+id);
    value_price_one = object_price_one.textContent;
    value_price_one_main = value_price_one.slice(0, -1);
    value_price_one_main = Number(value_price_one_main.replace('\xa0', ''));
    value_price_one_main = value_price_one_main / value; 
    value--;
    value_price_one_main = value_price_one_main * value;
    value_price_one_main = value_price_one_main.toString()
    object_price_one.textContent = value_price_one_main + " ₴";
    var elements = document.getElementsByClassName("product-price");
    sum = 0;
    for (let i = 0; i<elements.length; i++) {
      temp_value = elements[i].textContent;
      value_all = temp_value.slice(0, -1);
      value_all = Number(value_all.replace('\xa0', ''));
      sum = sum + value_all;
    }
    var total_price = document.getElementById("sum_price-number");
    total_price.textContent = sum.toString() + " ₴";
  }
  
  object.value = value;
}