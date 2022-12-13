// Exercise 1: Using array destructuring, take the first two items from the array and store them in a variable

const names = [nameOne, nameTwo, nameThree] = ['John', 'Jacob', 'Jingleheimer'];
// => John Jacob
console.log(nameOne, nameTwo)


// Destructuring Functions
// Exercise 2: Destructure the first two items returned from the function and store them in a variable

const foo = () => [1, 2, 3];
// => 1 2
const [first, second] = foo();
console.log(first, second);


// Swapping Variables
// Exercise 3: Without creating a temporary variable, use destructuring to swap the value of the following variables
let a = 'Jack';
let b = 'Jill';
// your code
console.log('a:', b, 'b:',a);
// => a: Jill b: Jack

[a, b] = [b, a];
console.log('a:', b, 'b:',a);