// battleship game
// 1. create a 10x10 grid

function drawGrid()
{
  let rows = [getLabelRow(), getHorzLine()];
  for (let yCoordinate = 0; yCoordinate < gridSize; yCoordinate++)
  {
    rows.push(getCellRow(yCoordinate));
    rows.push(getHorzLine());
  }
  rows.reverse();
  for (let row of rows)
  {
    console.log(row);
  }
  getLabelRow();
}

// 2. create a ship
// 3. place the ship on the grid
// 4. fire at the ship
// 5. keep track of the number of hits
// 6. keep track of the number of misses
// 7. keep track of the number of shots
// 8. keep track of the number of sunk ships
// 9. keep track of the number of remaining ships
// 10. keep track of the number of remaining shots
// 11. keep track of the number of remaining hits 



