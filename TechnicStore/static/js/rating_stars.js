// var rating = JSON.parse(document.getElementById('rating').textContent);
// var id = JSON.parse(document.getElementById('id').textContent);

$(document).ready(function () {
  $('.rating').raty({
    path: "\ /static/js/raty/images",
    scoreName: 'rating',
    starOff: 'star-off.png',
    starOn: 'star-on.png',
    width: 285,
    score: function () {
      return $(this).attr('data-score');
    }
  });
});

// aboba('#star'+id)

// function aboba(name) {
//   console.log("aboab")
//   $(name).raty({path: "\ /static/js/raty/images",  starOff: 'star-off.png',
//   starOn: 'star-on.png', readOnly: true, score: parseInt(rating) });
// }


