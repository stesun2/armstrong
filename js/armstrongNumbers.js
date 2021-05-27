// How can you make this more scalable and reusable later?

exports.findArmstrongNumbers = function(num) {
    let numArr = Array.from(num.toString());
    //create value for arr length
    console.log(numArr)
    let numArrLength = numArr.length;
    let result = 0;
    for (let i = 0; i < numArrLength; i++) {
      if (numArrLength > 1) {
        result += numArr[i] ** numArrLength;
      } else {
        result += numArr[i] ** 1;
      }
    }
    return result;
     //iterate through numArr
    //if arr length is greater than 1 power that by length else power that by 1
  };

console.log(exports.findArmstrongNumbers(12))