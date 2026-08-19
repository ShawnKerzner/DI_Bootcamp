for (let temp = 0; temp < 5; temp++) {
    console.log(temp + ": Institute!")
}

// this is what is happening in the loop above:
var temp = 0;                       //varialble_initialize (runs once)
console.log(temp + ": Institute!"); //- condition satisfies
temp = 1;                               //- variable incremented
console.log(temp + ": Institute!");
temp = 2;
console.log(temp + ": Institute!");
temp = 3;
console.log(temp + ": Institute!");
temp = 4;                               //-
console.log(temp + ": Institute!"); //- condition breaks