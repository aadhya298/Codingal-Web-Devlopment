var prop={
    greetings:"Hii" ,
    wishes:"welcome to" ,
    platform:"Codingal",
    about:"offers various coding courses"
}

var embedd= document.getElementById("pId")
embedd.innerHTML= prop.greetings+" "+prop.wishes+" "+prop.platform

var embedd2= document.getElementsByClassName("pClass")[1]
var data = prop.platform+" "+prop.about
embedd2.innerHTML= data


console.log(Math.sqrt(64));
console.log(Math.abs(-7.8));
console.log(Math.cbrt(-125));

function abc(){
    console.log(arguments[1]);
    console.log(arguments[3]);
    console.log(arguments[0]);
    console.log(arguments[2]);
}

abc(8,2,13,7);