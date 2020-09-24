const data = $('#hello').text();
$.post('https://fourtonfish.com/hellosalut/?lang=fr', data, function (data) {
  $('#hello').text(data.hello);
});
