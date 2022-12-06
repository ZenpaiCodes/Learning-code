// Exercise 1:

// Write a JavaScript program to get the difference between a given number and 27
// If the number is greater than 27 return double the absolute difference.

numOne = prompt("Enter a number: ");
numOne = parseInt(numOne);
numbTwo = 27;

if (numOne > numbTwo) {
    console.log((numOne - numbTwo) * 2);
} else {
    console.log(numbTwo - numOne);
}

// Exercise 2:

// Write a JavaScript program to compute the sum of the two given integers.
// If the two values are same, then returns triple their sum.

inputOne = prompt("Enter a number: ");
inputOne = parseInt(inputOne);
inputTwo = prompt("Enter another number: ");
inputTwo = parseInt(inputTwo);

if (inputOne === inputTwo) {
  console.log((inputOne + inputTwo) * 3);
} else {
  console.log("The two values are different.")
}

// Exercise 3:

// Write a JavaScript program to check two given numbers and 
// return true IF one of the number is 40 OR if their sum is 40. - else return false

giveNumOne = prompt("Enter a number: ")
giveNumOne = parseInt(giveNumOne)
giveNumTwo = prompt("Enter a number: ")
giveNumTwo = parseInt(giveNumTwo)

if ((giveNumOne + giveNumTwo) === 40) {
  console.log("Congratulations! result is 40!")
} else if (giveNumOne || giveNumTwo === 40) {
  console.log("Nice, one of the values is 40.")
} else {
  console.log("Wrong answer")
}

// Exercise 4:

// Create a function that takes a String as a parameter.
// Return the sum of any integers that are in the string.
// Example:
// Given "GH2U87A" you would return the value 17 (2 + 8 + 7).
// If there are no numbers in the string return 0.
// Post your solution in #projects channel of the chatroom

let str = prompt("Enter a string: ");

function sumOfIntegers(str) {
  let sum = 0;
  for (let x = 0; x < str.length; x++) {
    if (str[x] === "0") {
      sum += 0;
    } else if (str[x] === "1") {
      sum += 1;
    } else if (str[x] === "2") {
      sum += 2;
    } else if (str[x] === "3") {
      sum += 3;
    } else if (str[x] === "4") {
      sum += 4;
    } else if (str[x] === "5") {
      sum += 5;
    } else if (str[x] === "6") {
      sum += 6;
    } else if (str[x] === "7") {
      sum += 7;
    } else if (str[x] === "8") {
      sum += 8;
    } else if (str[x] === "9") {
      sum += 9;
    }
  }
  return sum;
}

console.log(sumOfIntegers(str));