// Object constructor !!!BEST PRACTICE!!! this is reusable code:
function Person(name, age) {
  this.name = name;
  this.age = age;
  this.greeting = function() {
    return `Hello, my name is ${this.name} and I am ${this.age} years old.`;
  }
}

console.log(new Person('Angie', 21));
console.log(new Person('Catalina', 8));
console.log(new Person('Gabriela', 7));

let humans = [];

humans.push(new Person('Melisa', 41));
humans.push(new Person('Lorena', 58));
humans.push(new Person('Juan', 27));

for (let i = 0; i < humans.length; i++) {
  console.log(humans[i].greeting());
}



// example 2 another way to create an object:
let person = {
  firstName: 'Zulk',
  lastName: 'Unknown',
  age: 23,
  hobbies: ['hunting', 'collecting swords', 'writing'],
  face: {
    hair: 'black',
    eyes: 'hazel',
  },  
  greeting: function() {
    return `Hello, my name is ${this.firstName} ${this.lastName} and I am ${this.age} years old.`;
  }  
}  

console.log(person['firstName']);
console.log(person['greeting']());
console.log(person);

// example 3 another way to create an object:
let personTwo = new Object();
let personThree = {};
//this is too repetitive
personThree.name = 'Xeck';
personThree.age = 23;
personThree.greeting = function() {
  return `Hello, my name is ${this.name} and I am ${this.age} years old.`;
}  

console.log(personTwo);
console.log(personThree);
console.log(personThree.greeting());


