// const ages = (year) => year > 2000 ? console.log("You are in the 21 centrury") : console.log("You live in the middle ages");
// ages(2001)

const add = a => b => c => d => a + b + c + d;

const result = add(2)(3)(4)(5)
console.log(result)