// JS Arrays

// Arrays are a special type of object that can hold multiple values
// Arrays are indexed starting at 0
// Arrays are mutable

let tvShows = [
  'The Office', 
  'Friends', 
  'The Simpsons', 
  'The Flash', 
  'The Big Bang Theory'];

// Empty array
var userSavedMovies = [];
// Add an item to the end of an array
userSavedMovies.push('The Matrix');
userSavedMovies.push('The Notebook');
userSavedMovies.push('The Lion King');

// Accessing elements in an array
console.log(tvShows[0]); // The Office

console.log(userSavedMovies);
console.log(userSavedMovies.length);


// ARRAY FILTERS
// example 1:
var numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

var filtered = numbers.filter(function(num, index) {
  console.log(index);
  return num >= 5;
});

console.log(filtered)

// example 2:
var classRm = {
  grade: '5th grade',
  students: [
    { name: 'John', score: 100 },
    { name: 'Jane', score: 95 },
    { name: 'Joe', score: 62 },
    { name: 'Jill', score: 79 },
  ]
}

var topStudents = classRm.students.filter(function(student) {
  return student["score"] >= 90;
});

console.log(topStudents);

// ARRAY reduce method
// example 1:
numbersExample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

var sum = numbersExample.reduce(function(accumulator, currentValue) { // accumulator is the sum of all the previous values 
  return accumulator + currentValue;
}, 0); // 0 is the initial value of the accumulator


// ARRAY map method
// example 1:
var classRoom = {
  grade: '6th grade',
  students: [
    { name: 'Cate', score: 100 },
    { name: 'Gaby', score: 100 },
    { name: 'Joe', score: 62 },
    { name: 'Jill', score: 79 },
  ]
}

var helloStudents = classRoom.students.map(function(student) {
  return 'Hello ' + student.name;
});

console.log(helloStudents);