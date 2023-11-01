// This script adds, removes and clears li from a list for each click
$(document).ready(function () { 
  $('#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('#remove_item').click(function () {
    $('UL.my_list li:last').remove();
  });
  $('#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
