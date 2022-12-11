// regular function
function addFunction(a, b) {
    return a + b;
}
console.log(addFunction(1, 2));

// arrow function
const addArrowFunctionOne = (x, y) => {
    return x + y;
}
console.log(addArrowFunctionOne(5, 8));

// arrow function with single line
const addArrowFunctionTwo = (i, c) => i + c;
console.log(addArrowFunctionTwo(10, 3));

// arrow function with single parameter
const addArrowFunctionThree = w => w + 1;
console.log(addArrowFunctionThree(10));

// arrow function with no parameter
const addArrowFunctionFour = () => 1 + 1;
console.log(addArrowFunctionFour());

// arrow function with no parameter and multiple lines
const addArrowFunctionFive = () => {
    const g = 1;
    const k = 2;
    return g + k;
}
console.log(addArrowFunctionFive());

// MORE examples
// EXAMPLE # 1: Adding a last name function using arrow function
const names = ['Andrew', 'Jen', 'Jess'];
/* const fullNames = names.map(function(name) {
    return name + ' Smith';
}); */
const fullNames = names.map((name) => name + ' Smith');
console.log(fullNames);

// EXAMPLE # 2: create objcts using arrow function from an array
const carCategory = 'Super car';

const cars = ['maserati', 'ferrari', 'lamborghini', 'bugatti'];

const displayWindow = cars.map((car, i) => ({carName: car, carCategory: carCategory, displaySection: i + 1 }));
console.table(displayWindow);

// EXAMPLE # 3: using arrow function on array with numbers 
const ageOfPlayers = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30];

const overTwentyOne = ageOfPlayers.filter((age) => age > 21);
console.log(overTwentyOne);

// EXAMPLE # 4: arrow function and 'this' keyword
const person = {
    name: 'Andrew',
    cities: ['Philadelphia', 'New York', 'Dublin'],
    printPlacesLived() {
        return this.cities.map((city) => this.name + ' has lived in ' + city);
    }
};