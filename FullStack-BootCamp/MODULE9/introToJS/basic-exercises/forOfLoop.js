// Practice 1: Create a loop that runs through each item in the fruits array.
const fruits = ['apple', 'banana', 'orange', 'watermelon'];

for (let fruit of fruits) {
  console.log(fruit);
};

// Practice 2: Create a loop that runs as long as i is less than 22, but increase i with 2 each time.
const num = [];

for (let i = 0; i < 22; i++) {
  i += 2;
  num.push(i)
  if (i === 20) {
    break;
  }
};

console.log(num);
