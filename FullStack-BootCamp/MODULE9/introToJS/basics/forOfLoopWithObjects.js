// for of loops with objects (objects are not iterable)
const warrior = {
  name: 'Zulk',
  power: 'Super Strength',
  level: 100,
  health: 999999
};

for(let key in warrior) {
  console.log(`${key}: ${warrior[key]}`);
};
