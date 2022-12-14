
const competitors = new Set();

competitors.add('John');
competitors.add('Mary');
competitors.add('Nancy');

const competed = competitors.values();

console.log(competed);

competed.next(); 

console.log(competed);

competed.next();

console.log(competed);

competed.next();