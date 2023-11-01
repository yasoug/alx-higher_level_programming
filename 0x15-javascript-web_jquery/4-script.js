// This script toggles the class of header elmt when DIV#toggle_header clicked
$(document).ready(function () {
  $('#toggle_header').click(function () {
    $('header').toggleClass('red green');
  });
});
