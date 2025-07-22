function checkvalidation(){
    var inp= document.getElementById("num");

    if(!inp.checkValidity()){
        document.getElementById("id1").innerHTML= inp.validationMessage;
    }
    else{
        document.getElementById("id1").innerHTML= "Input is fine"
    }
}