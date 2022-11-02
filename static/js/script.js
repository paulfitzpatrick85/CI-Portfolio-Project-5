setTimeout(function() {
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3000);
        


// Remove item and reload on click
$('.remove-item').click(function(e) {
    var csrfToken = "{{ csrf_token }}";
    var itemId = $(this).attr('id').split('remove_')[1];
    var url = `/remove/${itemId}/`;     
    var data = {'csrfmiddlewaretoken': csrfToken};

    $.post(url, data)
     .done(function() {
         location.reload();
     });
})

$('.carousel').carousel({
    interval: 2000
  })




