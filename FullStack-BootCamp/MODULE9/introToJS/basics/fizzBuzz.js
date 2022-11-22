let numbers = [];

// for loop to push numbers 1-100 into the array
for (let x = 1; x <= 100; x = x +1) {
  numbers.push(x);
}

// For each multiple of 3, print "Fizz" instead of the number.
// For each multiple of 5, print "Buzz" instead of the number.
// For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.

for (let x = 0; x < numbers.length; x = x + 1) {
  if (numbers[x] % 3 === 0 && numbers[x] % 5 === 0) {
    console.log("FizzBuzz");
  } else if (numbers[x] % 3 === 0) {
    console.log("Fizz");
  } else if (numbers[x] % 5 === 0) {
    console.log("Buzz");
  } else {
    console.log(numbers[x]);
  }
}