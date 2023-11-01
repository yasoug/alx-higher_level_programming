// This script fetches and prints how to say “Hello” depending on the language
$(document).ready(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/?lang=';
  $('#btn_translate').click(function () {
    const code = $('#language_code').val();
    $.get(url + code, function (data) {
      $('#hello').text(data.hello);
    });
  });
});
