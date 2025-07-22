function validation(){
    var v= document.forms["form1"]["name"].value;

    if(v==""){
        alert("Please fill out the given fields")
        return false;
    }
}