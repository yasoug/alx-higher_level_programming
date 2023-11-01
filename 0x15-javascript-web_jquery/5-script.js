// This script adds li element to a list when DIV#add_item is clicked
$(document).ready(function () {
  $('#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
});
