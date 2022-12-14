// map()
const people = new Map();

people.set('thisIsTheKey', 1); // set() method
people.set('thisIsTheKey2', 2);
people.set('thisIsTheKey3', 3);

console.log(people);

console.log(people.get('thisIsTheKey'));

console.log(people.size);

console.log(people.has('thisIsTheKey'));

people.delete('thisIsTheKey3');

console.log(people);

// loop through map
people.forEach((value, key) => {
  console.log(key, value);
});

// for of loop
for (let [key, value] of people) {
  console.log(key, value);
};
