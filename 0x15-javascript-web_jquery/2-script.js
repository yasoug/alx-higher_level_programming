// This script updates the text color when the user clicks on the tag DIV#red_header
$(document).ready(function() {
  $('#red_header').click(function () {
    $('header').css('color', '#FF0000');
  });
});
