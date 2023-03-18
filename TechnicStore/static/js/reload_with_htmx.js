// function saveState() {
//     var state = {
//       html: document.body.innerHTML,
//     };
//     history.pushState(state, '', window.location);
//   }
  
//   htmx.on('htmx:afterOnLoad', function(event) {
//     saveState();
//   });
  
//   window.addEventListener('popstate', function(event) {
//     if (event.state && event.state.html) {
//       document.body.innerHTML = event.state.html;
//     }
//   });
$(document).ready(function() {
  $('.checkbox_sort').on('change', function() {
    $('.checkbox_sort').not(this).prop('checked', false);
  });
});