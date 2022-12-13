// ES6 Object literal upgrades 
const make = 'Honda';
const model = 'Accord';
const year = 2020;

// Old way
const car = {
    make: make,
    model: model,
    year: year
};

// New way
const newCar = {
    make,
    model,
    year
};

console.log(car);
console.log(newCar);


const makeSuperCar = (make, model, year) => ({
    make,
    model,
    year
});

console.log(makeSuperCar('Lamborghini', 'Aventador', 2020));