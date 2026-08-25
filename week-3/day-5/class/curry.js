function curry(fn) {
    return function curried(...args) {
        if (args.length >= fn.length) {
            console.log("Inside IF:", args)
            return fn(...args);
        }
        console.log("Outside IF:", args)
        return (...more) => curried(...args, ...more);
    };
}

function add3(x, y, z) {
    return x + y + z;
}

function add6(a, b, c, d, e, f) {
    return a + b + c + d + e + f
}

const curriedAdd3 = curry(add3);
const curriedAdd6 = curry(add6);

console.log(curriedAdd3(1)(2)(3));
console.log(curriedAdd3(1, 2)(3));
console.log(curriedAdd3(1, 2, 3));
console.log(curriedAdd6(1, 2, 3, 4, 5, 6));
console.log(curriedAdd6(1, 2, 3)(4, 5, 6));
console.log(curriedAdd6(1)(2, 3)(4, 5, 6));
console.log(curriedAdd6(1)(2, 3)(4, 5)(6));
