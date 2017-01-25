var arm = require("./armstrongNumbers");

function createArrayOfNum(maxValue) {
  Array.apply(null, {length: maxValue}).map(Number.call, Number)
}

console.log(arm.findArmstrongNumbers([0]) === [0]);
console.log(arm.findArmstrongNumbers(createArrayOfNum(7)) === [0, 1, 2, 3, 4, 5, 6, 7]);
console.log(arm.findArmstrongNumbers(createArrayOfNum(99)) === [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]);
console.log(arm.findArmstrongNumbers(createArrayOfNum(999)) === [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]);
