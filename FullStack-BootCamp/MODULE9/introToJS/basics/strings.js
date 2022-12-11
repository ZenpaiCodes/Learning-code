// regular string
let username = 'John';
console.log(username);

// template string
let usernameTwo = `Carl`;
let tallOrSmall = true;

console.log(`Hello ${usernameTwo}! How are you?`);

console.log(`${usernameTwo} you are ${21 + 1} years old.`);

console.log(`${usernameTwo} is the ${tallOrSmall ? 'tallest' : 'smallest'} person in the room. 
By pressing ENTER i can create a line space`); // ternary operator

// New string methods
const devslopes = 'Week 1 iOS Academy';
const accountNumber = '000129563345SAV';
const emoji = '😀 🔥';

console.log(devslopes.startsWith('Week')); // startsWith returns a boolean -> true || false
console.log(devslopes.startsWith('iOS', 7)); // startsWith takes a second argument for index position, it returns a boolean
console.log(devslopes.endsWith('Academy')); // endsWith returns a boolean
console.log(accountNumber.endsWith('SAV')); 
console.log(accountNumber.includes('9')); // includes checks if a string is included in another string, it returns a boolean
console.log(accountNumber.includes('%')); 
console.log(emoji.repeat(3)); // repeat repeats a string a number of times, it returns a string


