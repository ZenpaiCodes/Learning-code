
const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
})

readline.question('What operation would you like to perform? ', (operation) => {
  readline.question('Please enter the first number: ', (firstNumber) => {
    readline.question('Please enter the second number: ', (secondNumber) => {
      if (operation === '/' || operation === '*' || operation === '-' || operation === '+') {
        if (isNaN(firstNumber) || isNaN(secondNumber)) {
          console.log('This is not a number')
        } else {
          if (operation === '/') {
            console.log(`The result is: ${firstNumber / secondNumber}`)
          } else if (operation === '*') {
            console.log(`The result is: ${firstNumber * secondNumber}`)
          } else if (operation === '-') {
            console.log(`The result is: ${firstNumber - secondNumber}`)
          } else if (operation === '+') {
            console.log(`The result is: ${firstNumber + secondNumber}`)
          }
        }
      } else {
        console.log('That is not a valid operation')
      }
      readline.close()
    })
  })
})