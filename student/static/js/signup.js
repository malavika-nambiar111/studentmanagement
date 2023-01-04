var nam = document.getElementById('name')
var email = document.getElementById('email')
var phno = document.getElementById('phno')
var pass1 = document.getElementById('pass1')
var pass2 = document.getElementById('pass2')

function validname(){
    var fn = nam.Value;
    if (isNaN(fn)){
        nam.className = "success";
        document.getElementById("text").innerHTML = "";
    }
    else{
        nam.className = "error";
        document.getElementById("signup").disabled = true;
        document.getElementById("text").innerHTML = "please enter a name";
    }
}

function validmail(){
    var mail = email.value;
    var re = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    if (re.test(mail)){
        email.className = "success";
        document.getElementById("text").innerHTML = "";
    }
    else{
        email.className = "error";
        document.getElementById("text").innerHTML = "please enter a valid mail id";
    }
}

function validphno(){
    var num = phno.value;
    if (isNaN(num)){
        phno.className = "error";
        document.getElementById("signup").disabled = true;
        document.getElementById("text").innerHTML = "please enter a valid phone number"
    }
    else{
        var num1=num.length;
        if (num1==10){
            phno.className = "success";
            document.getElementById("text").innerHTML = "";
        }
        else{
        phno.className = "error";
        document.getElementById("text").innerHTML = "please enter a valid phone number";
        }
    }
}

function validpass() {
    var pass1 = pass1.value.length;
    if(pass1 >= 8 & pass1 <= 16){
        pass1.className = "success";
        document.getElementById("text").innerHTML = "";
    }
    else{
        pass1.className = "error";
        document.getElementById("signup").disabled = true;
        document.getElementById("text").innerHTML = "password length must be greater than 8 characters and not exceed 15";
    }
}

function validpassconfirm(){
    var pass = pass1.value;
    var passc = pass2.value;
    if (pass == passc){
        pass2.className = "success";
        document.getElementById("text").innerHTML = "";
        document.getElementById("signup").disabled = false;
    }
    else{
        pass2.className = "error";
        document.getElementById("signup").disabled = true;
        document.getElementById("text").innerHTML = "password not match";
    }
}

document.getElementById("signup").disabled = true;