$(document).ready(function() {
  $('.checkbox_sort').on('change', function() {
    $('.checkbox_sort').not(this).prop('checked', false);
  });
});