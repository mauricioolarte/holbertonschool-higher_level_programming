/* script that fetches from https://fourtonfish.com/hellosalut/?lang=fr and
displays the value of hello from that fetch in the HTML’s tag DIV#hello.
*/
const data = $('#hello').text();
$.post('https://fourtonfish.com/hellosalut/?lang=fr', data, function (data) {
  $('#hello').text(data.hello);
});
