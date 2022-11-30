setTimeout(function() {
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3000);
        

// from b/a + changed
// Remove item and reload on click
$('.remove-item').click(function(e) {
    // var csrfToken = "{{ csrf_token }}";
    var itemId = $(this).attr('id')
    var url = `/remove/${itemId}/`;     
    // var data = {'csrfmiddlewaretoken': csrfToken};

    $.post(url)   // $.post(url, data)
     .done(function() {
         location.reload();
     });
})

$('.carousel').carousel({
    interval: 2000
  })




