setTimeout(function() {
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3000);
        

// from b/a + changed
// Remove item and reload on click
$('.remove-item').click(function(e) {
    var itemId = $(this).attr('id')
    var url = `/remove/${itemId}/`;     
    $.post(url)   
     .done(function() {
         location.reload();
     });
})

$('.carousel').carousel({
    interval: 2000
  })




