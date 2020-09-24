
$('#toggle_header').click(function () {
  if ($('header').attr('class') === 'green') {
    $('header').toggleClass('red');
  } else {
    $('header').toggleClass('green');
  }
});
