setTimeout(function() {
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3000);
        
function edit() {
    alert("Your Band Information Has Been Updated./ You Can Now Return To Your Profile To View The Changes.");
}


// $('#deleteModal{{ review.id }}').on('shown.bs.modal', function () {
//     $('#deleteModal{{ review.id }}').trigger('focus')
//   })

// Remove item and reload on click
$('.remove-item').click(function(e) {
    var csrfToken = "{{ csrf_token }}";
    var itemId = $(this).attr('id').split('remove_')[1];
    var url = `/remove/${itemId}/`;     //url to be made later
    var data = {'csrfmiddlewaretoken': csrfToken};

    $.post(url, data)
     .done(function() {
         location.reload();
     });
})


$('.carousel').carousel({
    interval: 2000
  })


