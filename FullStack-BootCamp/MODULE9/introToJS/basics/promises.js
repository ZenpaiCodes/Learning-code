// Promises 
// Promises are used to handle asynchronous operations in JavaScript.
const pokemon = fetch('https://pokeapi.co/api/v2/pokemon/pikachu');

pokemon
.then((data) => data.json())
.then((data) => console.log(data))
.catch((err) => console.log(err)); 


// work with multiple promises
const youtubePost = { id: 1, comment: 'Promises in JS' };
const hobbies = ['Sports', 'Cooking'];

const post = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve(youtubePost);
  }, 2000);
});

const hobby = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve(hobbies);
  }, 1000);
});

Promise
  .all([post, hobby]) // returns an array of the results
  .then((result) => console.log(result));