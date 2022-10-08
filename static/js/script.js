setTimeout(function() {
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3000);
        
function edit() {
    alert("Your Band Information Has Been Updated./ You Can Now Return To Your Profile To View The Changes.");
}
