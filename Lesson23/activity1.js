var work="JS Code";
var array=[2,3,6,8,9,"A","B","H","Q", function(){console.log(work)}];

console.log(array[3]);   // 8 will be printed as indexing is done from 0
var a= array[9];
a();

array.pop();
console.log(array);

console.log(array.join(" ~ "));

// Call Stack
function number(){
   return Math.floor(Math.random()*10)
   
}

function divide(){
    q= number()+2
    console.log(q)
}
divide();