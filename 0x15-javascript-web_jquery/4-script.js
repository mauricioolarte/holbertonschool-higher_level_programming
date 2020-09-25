/*
script that toggles the class of the HTML tag HEADER when
the user clicks on the tag DIV#toggle_header.
*/
$('#toggle_header').click(function () {
  if ($('header').attr('class') === 'green') {
    $('header').toggleClass('red');
  } else {
    $('header').toggleClass('green');
  }
});
