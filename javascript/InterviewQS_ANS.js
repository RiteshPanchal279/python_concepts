// 1) Wxplain ehat a callback function is and provide a simple example.

// Ans :- A callback function is a function that is passed to another function as an argument and is executed after some operation has been completed.Below is an example of a simple callback fuction that logs to the console after some operations have been completed.

function modifyArray(arr,callback){
   arr.push(100);
   callback();
}

let arr=[2,4,5,6,7];

modifyArray(arr,function(){
   console.log("Array has been modified: ",arr);
})

// Q 2) How would you check if a number is an integer?
// Ans:- A very simple way to check if number is a decimal or integer is to soo if there is a remainder left whent you devide by 1;

function isInt(num){
   return num % 1 === 0;
}

console.log(isInt(4)) // true
console.log(isInt(1.24))//false
console.log(isInt(0.9))//false

// Q 3) Make this Work duplicate([1,2,3,4,5])

function duplicate(arr){
   return arr.concat(arr);
}

const ans = duplicate([1,2,3,4,5])
console.log(ans)

// Q 4) curry function

function mul(x){
   return function(y){
      return function(z){
         return x * y * z;
      }
   }
}

console.log(mul(2)(3)(5))