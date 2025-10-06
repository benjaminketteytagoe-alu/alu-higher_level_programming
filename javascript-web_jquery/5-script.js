// Add click event listener to DIV#add_item using jQuery
$('#add_item').click(function() {
  $('ul.my_list').append('<li>Item</li>');
});
