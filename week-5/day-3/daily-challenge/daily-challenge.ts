function validateUnionType(value: any, allowedTypes: string[]): boolean {
    const valueType = typeof value;
    for ( let type of allowedTypes) {
        if (valueType === type) {
            return true;
        }
    }
    return false;
}
const myList: string[] = ["string", "number"];
console.log(validateUnionType("shawn", myList));
console.log(validateUnionType(5, myList));
console.log(validateUnionType(false, myList));

