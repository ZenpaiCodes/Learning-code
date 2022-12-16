const readlineSync = require('readline-sync');

// battleship game 

// 1. When the application loads, print the text, "Press any key to start the game."
console.log(`
Press any key to start the game.`);
let startGame = readlineSync.keyInPause();

// 2. When the user presses a key, print the text, "Welcome to Battleship!"
console.log(`
                                         (   )
                                          ( )
                                  _________|__
                              _  |____________|  _
                       _=====| | | º º    º º | | |==== _
                 =====| |.---------------------------. | |====
   |-------------------'   .  .  .  .  .  .  .  .   '----------------/
     |        o           ·:*¨༺     ★      ༻¨*:·.        o          /
      |____________________________________________________________/
  ‿︵‿‿︵‿‿︵‿‿︵‿‿︵‿‿︵‿‿︵‿‿︵‿‿︵‿‿︵‿‿︵‿‿︵‿‿︵‿‿︵‿‿︵‿‿︵‿‿︵‿

                          Welcome to Battleship!
  `);

// 3. create a function to generate the battleship grid
const gridSize = readlineSync.questionInt(`How big do you want the grid to be? `);
const grid = generateGrid();

function generateGrid() {
  let grid = [];
  for (let i = 0; i < gridSize; i++) {
    grid.push([]);
    for (let j = 0; j < gridSize; j++) {
      grid[i].push('‿︵‿');
    }
  }
  return grid;
}
console.log(grid);

// 4. create coordinates for the battleship positioning 
let battleshipPosition = {
  x: Math.floor(Math.random() * gridSize),
  y: Math.floor(Math.random() * gridSize)
};
console.log(battleshipPosition);

// 5. user guesses the battleship position
let userGuess = {
  x: readlineSync.questionInt(`Guess the x coordinate: `),
  y: readlineSync.questionInt(`Guess the y coordinate: `)
};
console.log(userGuess);

// 6. create a function to check if the user guessed the battleship position
function checkGuess() {
  grid[userGuess.x][userGuess.y] = 'missed!';
  replaceGrid();
  console.log(grid);
  while (userGuess.x !== battleshipPosition.x || userGuess.y !== battleshipPosition.y) {
    userGuess = {
      x: readlineSync.questionInt(`Guess the x coordinate: `),
      y: readlineSync.questionInt(`Guess the y coordinate: `)
    };
    grid[userGuess.x][userGuess.y] = 'missed!';
    console.log(grid);
  }
}
checkGuess();

// 7. if user guessed the battleship position, replace grid '‿︵‿' with 'Σ■╬■>'
function replaceGrid() {
  if (userGuess.x === battleshipPosition.x && userGuess.y === battleshipPosition.y) {
    grid[battleshipPosition.x][battleshipPosition.y] = 'Σ■╬■>';
    console.log('You hit the battleship!')
    return grid;
  }
}
console.log(replaceGrid());












