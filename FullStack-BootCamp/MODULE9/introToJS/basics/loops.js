var animeShows = [
    "Naruto",
    "Bleach",
    "One Piece",
    "Dragon Ball Z",
    "Death Note",
];

for (var i = 0; i < animeShows.length; i++) {
  console.log(i);
}

// if 0 < 5, then run the code inside the loop
// if 1 < 5, then run the code inside the loop
// if 2 < 5, then run the code inside the loop
// if 3 < 5, then run the code inside the loop
// if 4 < 5, then run the code inside the loop
// if 5 < 5, then stop the loop


let toDoList = [
    { title: "Go to the gym", completed: true },
    { title: "Go to the market", completed: false },
    { title: "Go to the school", completed: true },
    { title: "Go to the office", completed: false },
    { title: "Go to the park", completed: true },
];

let completedItems = [];
let notDoneItems = [];

for (let x = 0; x < toDoList.length; x++) {
  if (toDoList[x].completed) {
    completedItems.push(toDoList[x]);
  }

  if (!toDoList[x].completed) { // if (toDoList[x].completed === false)
    notDoneItems.push(toDoList[x]);
  }
}

console.log(toDoList);
console.log(completedItems);
console.log(notDoneItems);

// while loop

let bottles = 99;

while (bottles > 0) {
  if (bottles !== 1) {
    console.log(bottles + " bottles of water on the wall");
    bottles--; // bottles = bottles - 1
  } else {  
    console.log(bottles + " bottle of water on the wall");
    bottles--;
  } 
}