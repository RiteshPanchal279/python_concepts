interface Student{
   name:String,
   code:String
}

let std1 = <Student>{};

std1.name="OKKKK"
std1.code="MY code"

console.log(std1.name)
console.log(std1.code)

// first do command :- tsc .\interface.ts
// second do command :- node .\interface.js
