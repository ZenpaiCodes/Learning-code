// refactoring 🇨ode 
const names = ['john', 'peter', 'bob', 'anna', 'kelly'];
const me = 'anna';

// Not DRY code
const isOnList = (name) => {
  if (name === names[0]) {
    console.log(`${name} is on the list`);
  } else if (name === names[1]) {
    console.log(`${name} is on the list`);
  } else if (name === names[2]) {
    console.log(`${name} is on the list`);
  } else if (name === names[3]) {
    console.log(`${name} is on the list`);
  } else if (name === names[4]) {
    console.log(`${name} is on the list`);
  } else {
    console.log(`${name} is not on the list`);
  }
};

isOnList(me);

// DRY code
const itIsOnList = (name, list) => {
  const onlist = list.includes(name);
  console.log(`${name} is ${onlist ? '' : 'not'} on the list`);
};

itIsOnList('Diego', names);
