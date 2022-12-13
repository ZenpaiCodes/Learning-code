// the for of loop
// for of loop is used to iterate over the values of an iterable object

const shoes = ['Nike', 'Adidas', 'Puma', 'Reebok', 'Fila'];

// for of loop. NEW WAY--------------------------------------
for(let shoe of shoes){
    console.log(shoe);
}








// for of loop. OLD WAY
for(let i = 0; i < shoes.length; i++){
    console.log(shoes[i]);
}

// or ||

// for of loop. OLD WAY
shoes.forEach((shoe) => { // cannot use break or continue
    console.log(shoe);
});

