// Prototypal Inheritance Review 
// Prototypal Inheritance is a way to create objects that inherit from other objects.
function Person(name, hobby) {
  this.name = name;
  this.hobby = hobby;
};

Person.prototype.greeting = function() {
  console.log(`Hi, my name is ${this.name} and I like ${this.hobby}`);
};

const person1 = new Person('John', 'Soccer');
const person2 = new Person('Jane', 'Basketball');

console.log(person1['name']);
console.log(person2);

