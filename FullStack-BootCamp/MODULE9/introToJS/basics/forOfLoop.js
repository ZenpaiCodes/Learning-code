// the for of loop
// for of loop is used to iterate over the values of an iterable object

const shoes = ['Nike', 'Adidas', 'Puma', 'Reebok', 'Fila'];

// for of loop. NEW WAY--------------------------------------
for(let shoe of shoes){
    console.log(shoe);
};

// return value with 📇 index
for(let shoe of shoes){
    console.log(shoe, shoes.indexOf(shoe));
};

// example sum total of arguments 
function addTotal() {
  let total = 0;
  for (let num of arguments) {
    total += num;
  }
  console.log(total);
  return total;
};

addTotal(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

// example for a loop with a string 
const fullName = 'Rafael Suarez';
for(let char of fullName){
    console.log(char);
};


