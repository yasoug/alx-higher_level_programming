// This script fetches and displays the value of hello in the html tag DIV#hello
$(document).ready(function () {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    type: 'GET',
    dataType: 'json',
    success: function (data) {
      $('#hello').text(data.hello);
    }
  });
});
