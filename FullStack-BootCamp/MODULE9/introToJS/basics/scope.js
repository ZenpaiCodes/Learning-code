// Javascript Scope

// Global Scope
var a = 1; // The whole window has access to this variable. Thus it can be accessed from anywhere in the window.
console.log(a);

if (true) {
  var a = '(a) value changed';
}
console.log(a);

// window.a = 'new value has been assign as a string'; // a has now changed it's value to a string.
// console.log(a);


// Local Scope
function myFunction(num) {
  var b = num + 200; // This variable is only accessible within the function.
  console.log(b);
}

var b = 3; // This is not changing the value of b in the function. It is creating a new variable b in the global scope.
console.log(b);

// to access the value of b in the function, we need to call the function.
myFunction(5);


// EXAMPLE #2  global scope vs local scope

let firstName = 'Gaby';

let userOne = {
  firstName: 'Cata',
  age: 8,
}

function userBDay(age) {
  let newAge = age + 1;
  userOne['age'] = newAge;
  console.log('Happy Birthday ' + userOne['firstName'] + ' you are now ' + newAge);
}

userBDay(userOne['age']);
console.log(userBDay);

// BLOCK SCOPE
// Block scope is the scope of a variable that is limited to a block of code.

// EXAMPLE #1
let y = 10;
if (true) {
  y = 20;
  if (true) {
    y = 'Hello';
    for (let i = 0; i <4; i++) {
      y = i;
      console.log(i);
    }
  }
}

console.log(y); // it will not print, as it is not accessible outside of the block.