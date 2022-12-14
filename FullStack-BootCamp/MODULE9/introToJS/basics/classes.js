// Classes 
// Classes are a template for creating objects. They encapsulate data with code to work on that data.

// Class Declaration
class Person {
  constructor(name, hobby) {
    this.name = name;
    this.hobby = hobby;
  }
  greeting() {
    console.log(`Hi, my name is ${this.name} and I like ${this.hobby}`);
  }

  extraFunction() {
    console.log('This is an extra function');
  }

  static staticFunction() {
    console.log('This function lives within the person class and its only accessible through the class');
  }
};

const person1 = new Person('John', 'Soccer');
const person2 = new Person('Jane', 'Basketball');

console.log(person1);
console.log(person2);
person1.extraFunction();
Person.staticFunction();

// -------------------------------------------------------------------

// Class Expression
const Student = class {
};