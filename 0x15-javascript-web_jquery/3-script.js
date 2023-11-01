// This script adds the class red to header when clicked on the tag DIV#red_header
$(document).ready(function() {
  $('#red_header').click(function () {
    $('header').addClass('red');
  });
});
