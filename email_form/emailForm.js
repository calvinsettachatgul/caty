window.onload = init;



function init(){
    console.log("javascript ready")
    addEmailListener();
}

function addEmailListener(){
    let emailForm = document.getElementById("email")
    let emailSubmitButton = document.getElementById("sendEmail")
    let sendCallback = function(event){
        event.preventDefault();
        console.log("email", emailForm.email.value);
        console.log("message", emailForm.message.value);
        window.open('mailto:' + emailForm.email.value);

    }
    emailSubmitButton.addEventListener('click', sendCallback);
}