let name,div;
({name,div}={name:"Ritesh",div:"One"})
console.log(name)
console.log(div)

// --------------------------------->

function average(...args){
   console.log(args)
   var sum = args.reduce((a,b)=>a+b);
   let avg = sum/args.length;
   return avg;
}

ans = average(1,2,3,4,5,6,7)
console.log("The average is :",ans)