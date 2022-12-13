// Spread Operator

// example create list of order
const skatePants = ['Volcom', 'Element', 'DC', 'Emerica']; 
const skateShoes = ['Vans', 'DC', 'Emerica', 'Nike SB'];

// in this case to avoid double shipping we have to convine both arrays
const order = [...skatePants, 'add extra item', ...skateShoes];
console.log(order);

const skaterDude = {
  name: 'Sude',
  shoes: ['DC', 'Supra'],
};

skaterDude.shoes = [...skaterDude.shoes, ...skateShoes];
console.table(skaterDude);

console.log(...skaterDude.shoes[2]); // took item from array and spread it "V a n s"

const comments = [
  {id: 1, text: 'Love this!'},
  {id: 2, text: 'Super good'},
  {id: 3, text: 'You are the best'},
  {id: 4, text: 'Ramen is my fav food ever'},
];

const id = 3;
const commentIndex = comments.findIndex(comment => comment.id === id);



// Exercise 1: Write a function called combineArrays that takes in two arrays as arguments, and returns a single array that combines both (using the spread operator).
combineArray = () => {
  const array1 = [1, 2, 3];
  const array2 = [4, 5, 6];
  const array3 = [...array1, ...array2];
  console.log(array3);
  return array3;
}
combineArray();


// Exercise 2: Write a function called addEveryOther that takes in any amount of arguments, and returns the sum of every other argument.
function addEveryOther() {
  let sum = 0;
  for (let i = 0; i < arguments.length; i += 2) {
    sum += arguments[i];
  }
  return sum;
}
console.log(addEveryOther(1, 2, 10, 3, 4, 5)); // 15


// CONTINUE with spreading into a Function
const dogs = ['bulldog', 'beagle', 'labrador'];
const moreDogs = ['poodle', 'pug', 'dalmation'];

const allDogs = [...dogs, ...moreDogs];
console.log(allDogs);


const greeting = (firstName, lastName) => {
  console.log(`Hello ${firstName} ${lastName}!`);
}

let fullName = ['Sude', 'Khan'];
greeting(...fullName);


// ...rest parameter in a function (and destructuring)
const currencyConverter = (rate, ...amounts) => { // ...amounts is a rest parameter (it collects all the arguments into an array)
  return amounts.map(amount => amount * rate);
};

const amounts = currencyConverter(1.1, 20, 30, 40, 50);
console.table(amounts);