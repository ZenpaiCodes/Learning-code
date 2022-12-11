// destructuring allows us to extract data from arrays and objects and assign them to variables
const zulk = {
  realName: 'Diego',
  lastName: 'Camacho',
  age: 30,
  urls: {
    social: {
    twitter: 'https://twitter.com/zulk',
    facebook: 'https://facebook.com/zulk',
    instagram: 'https://instagram.com/zulk',
    },
    web: {
      blog: 'https://zulk.com',
      portfolio: 'https://zulk.com/portfolio',
    }
  } 
}

console.log(zulk.realName);//regular access
console.log(zulk.urls.social.twitter);//regular access

//destructuring
const { realName, lastName, age, urls: { social: { twitter, facebook, instagram }, web: { blog, portfolio } } } = zulk;

console.log(`
----DESTRUTURING----
`);

console.log(realName);
console.log(lastName);
console.log(age);
console.log(twitter);
console.log(facebook);
console.log(instagram);


// Practice: Take the following object and store the name and youtube properties in their own variable.
console.log(`
EXERCISE: Practice: Take the following object and store the name 
and youtube properties in their own variable.
`);

const person = {
  userName: "Harry Mack",
  age: 30,
  expertise: "jaw-dropping visual freestyle rapping",
  youtube: "www.youtube.com/harrymack",
};

const {userName, youtube} = person;

console.log(userName);
console.log(youtube);


// destructuring ARRAYS
//methos # 1
const food = [first, second, third] = ['🍕 pizza', '🍔 burger', '🍟 fries'];
console.log(first);
console.log(second);
console.log(third);

//method # 2
const movies = ['The Matrix', 'The Notebook', 'The Avengers'];
const [firstMovie, secondMovie, thirdMovie] = movies;
console.log(firstMovie);
console.log(secondMovie);
console.log(thirdMovie);

// method # 3
const students = 'Diego, Carl, John, Zulk';
const [firstStudent, secondStudent, thirdStudent, fourthStudent] = students.split(', ');
console.log(firstStudent);
console.log(secondStudent);
console.log(thirdStudent);
console.log(fourthStudent);


// sawp variab🇱🇸 using destructuring
let working = 'cata';
let onBreak = 'gaby';

console.log('working:', working);
console.log('onBreak:', onBreak);

[working, onBreak] = [onBreak, working];

console.log('working:', working);
console.log('onBreak:', onBreak);

// FUNCTIONS() with destructuring
const cryptoConverter = (amount) => {
  const crypto = {
    BTC: amount / 20000,
    ETH: amount / 1200,
    LTC: amount / 80,
    XEM: amount / 0.20,
  }
  return crypto
}

const {BTC, ETH, LTC, XEM} = cryptoConverter(1000);

console.log(ETH)
