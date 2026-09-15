import _ from 'lodash'; // originally i did require as asked but this caused a bug as it can not run both es6 and full commonJS so i picked es6 and added type: module to the package.json
import { sum, product } from './math.js';

sum(6,7);
product(6,7);

const numbers = [1,2,3,4,5,6,7,8]

const total = _.sum(numbers);
const doubled = product(total, 2);
console.log(sum(doubled, total));