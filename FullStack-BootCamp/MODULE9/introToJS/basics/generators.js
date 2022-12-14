// Generators 
// Generators are functions that can be exited and later re-entered. Their context (variable bindings) will be saved across re-entrances.
function* generatorFunction() {
  let num = 0;
  yield num;
  num += 1;
  yield num;
  num += 1;
  yield num;
  yield 'I am a function runned: 1st time';
  yield 'I am a function runned: 2nd time';
  yield 'I am a function runned: 3rd time';
};

const testGeneratorFunction = generatorFunction();
console.log(testGeneratorFunction.next());