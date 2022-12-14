// Array.from() and Array.of()

// Array.from() - creates a new array from an array-like or iterable object
function addTotal() {
  const numbers = Array.from(arguments);
  return numbers.reduce((prev, next) => prev + next, 0);
}
const total = addTotal(18, 20, 53, 14, 59, 226, 17, 88, 3969, 510);
console.log(total);


// Array.of() - creates a new array instance from a variable number of arguments
const nums = Array.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
console.log(nums);
