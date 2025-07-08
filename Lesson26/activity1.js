class Info1{
    constructor(a,b,c){
        this.name=a
        this.grade=b
        this.age=c
    }

    school(){
        return 'Rishikesh International School'
    }
    static howIsYourSchool(){
        console.log('Absolutely Fine')
    }
}

class Info2 extends Info1{
    constructor(a,b,c,d){
        super(a,b,c)
        this.stream=d
    }
    hobbies(){
        return 'My hobbies are to read novels'
    }
}

var p= new Info1("Harry","X",14)
var q= new Info2("Emma","XI",16,"Maths")
console.log(p.name)
console.log(p.grade)
console.log(p.age)
console.log(p.school())
console.log("--------------now child class Info2--------------")
console.log(q.name)
console.log(q.grade)
console.log(q.age)
console.log(q.stream)
console.log('--------------------caling static methods--------------------')
console.log("By parent class")
Info1.howIsYourSchool()
console.log("By child class")
Info2.howIsYourSchool()