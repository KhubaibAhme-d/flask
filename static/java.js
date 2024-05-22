// $(document).ready(function(){

//     $('#butt').on('click', function(e){
//         e.preventDefault();
// name = $('#name').val();
// $.post('/test', {name: name}, function(data){
//     // if (data.status == 200) {
//         console.log("Yes")

//     // }
//         })
//     })

// })

$(document).ready(function () {
    $("#login").submit(function (event) {
        $(".error-message").remove();
        // Prevent default form submission
        event.preventDefault();
        name = $('#usr').val();
        if (!name) {
            $("<span class='error-message'>Please enter a username.</span>").insertAfter("#usr");
            return;
        }
        // console.log(name)   
        $.post('/test', { name: name }, function (data) {
            // console.log(data)
            if (data.status == 200) {
                console.log("success");
                window.location.href = "http://127.0.0.1:5000/welcome";
            }
            // Log "success" to the console
            else {
                $("<span class='error-message'>Please enter Correct username.</span>").insertAfter("#buttt");
            }
        });
    });
});
