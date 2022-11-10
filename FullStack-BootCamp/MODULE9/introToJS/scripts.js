// SECTION -1: JavaScript is Fun!
    // Primitive / Value Types
var firstName = 'Diego'; // String
var age = 35; // Number
var clever = true; // Boolean
var favFood; // Undefined - no value assigned
var toiletPaper = null; // Null - can receive any value of any type and can reset.

console.log('Value: ', firstName);
console.log('Type: ',typeof firstName);
console.log('Value: ', age);
console.log('Type: ',typeof age);
console.log('Value: ', clever);
console.log('Type: ',typeof clever);
console.log('Value: ', favFood);
console.log('Type: ',typeof favFood);
console.log('Value: ', toiletPaper);
console.log('Type: ',typeof toiletPaper);



// Reference Types / Structural Types
// create an object
var person = {
  // properties of the object
  firstName: 'Angie',
  lastName: 'Camacho',
  age: 35,
  longHair: true,
  favFood, // Undefined - no value assigned
}

console.log('Value: ', person);
console.log('Type: ',typeof person);

// create an array
var students = ['Cata', 'Gaby', 'Maria'];

console.log('Value: ', students);
console.log('Type: ',typeof students);

// create a function
var myFunction = function() {
  // run some code
}

console.log('Value: ', myFunction);
console.log('Type: ',typeof myFunction);

// SECTION 2: Strings
let userName = 'Matthew';
let userLastName = 'Martin';
let userAge = 30;
const gender = 'male';

// Strins concatination
const userInfo = 'Welcome ' + userName + ' ' + userLastName + '.' + 'You are ' + age + ' ' + 'old.' + 'and you are a ' + gender + '.'

console.log(userInfo)
console.log(userInfo.length)

// SECTION 3: Numbers
// in JS numbers are numbers. No separation/distinction on integers or decimals.
// PEMDAS: Parentheses, Exponents, Multiplication, Division, Addition, Subtraction
let totalUsers = 50;
let totalBill = 10.50;
let numPlusStrNum = '10' * 10; // can use string num as num, 
                               // as long as (+) is not used, otherwise it will be a string.
console.log(numPlusStrNum)

const numCalculationOne = 66 * totalUsers;
const numCalcTwo = totalBill % 2;

console.log(numCalculationOne);
console.log(numCalcTwo);

// Method	Description
// toString()	Returns a number as a string
// toExponetial()	Returns a number written in exponential notation
// toFixed()	Returns a number written with a number of decimals
// toPrecision()	Returns a number written with a specified length
// ValueOf()	Returns a number as a number

