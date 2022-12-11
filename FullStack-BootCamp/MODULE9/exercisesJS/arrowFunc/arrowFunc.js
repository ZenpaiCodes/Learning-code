// Exercise 1: Write an arrow function that returns the string "Hello Radness".
const printStr = () => console.log('Hello Radness');
printStr();


// Exercise 2: Write an arrow function that expects an array of integers, and returns the sum of the elements of the array. Use the built-in method reduce() on the array argument.
const array1 = [10, 235, 32, 94];
const sumWithInitial = array1.reduce((a, c) => a + c, 0); // a: accumulator, c: current value, 0: initial value
console.log(sumWithInitial);


// Exercise 3: Run the following code with Node to see the result. Then refactor any of the capable function(s) with arrow functions. The code should still work 😉
// MISSING
const Animal = function(animal, sound, delay) {
  this.animal = animal;
  this.sound = sound;
  this.delay = delay;
}

Animal.prototype.greet = function() {
  setTimeout =(function() {
    console.log(`Hi, I am a ${this.animal}...${this.sound}`);
  }.bind(this), this.delay);
};

const dog = new Animal('Dog', 'Bark', 3000);
const cat = new Animal('Cat', 'Meow', 200);
dog.greet();
cat.greet();

