class Rectangle {
    constructor(height, width) {
        this.height = height;
        this.width = width;
    }

    // calcArea() {
    //     return this.height * this.width;
    // }

    get area() {
        return this.height * this.width
    }

    set area(factor) {
        this.width = this.height * this.factor
    }
}

const square = new Rectangle(10, 10);
console.log(square.calcArea());
console.log(square);