// set()
// set() is a method that adds a new element to a Set object.
// it can only have 1 unique value
const names = new Set();
names.add('John');
names.add('Mary');
names.add('Nancy');

// values()
console.log(`
This is the value(): ${names.values()}`); 

console.log(names);
console.log(`
This is adding .size: ${names.size}`); // 3

// has()
console.log(`
This is the has(): ${names.has('John')}
`); // true

// delete item 
names.delete('John');
console.log(names);

// clear all items
names.clear();
console.log(names);
