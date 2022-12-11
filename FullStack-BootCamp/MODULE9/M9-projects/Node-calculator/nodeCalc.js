// import the readline-sync module
// Ask the user, "What operation would you like to perform?"
// Then the user enters one of these options: "/" "*" "-" "+"
// After the user enters a valid operation, ask the user, "Please enter the first number"
// The user then enters the first number. If the user enters something that is not a number, print: “This is not a number” and then re-ask the question
// After a valid number is entered, ask the user, "Please enter the second number". Perform the same error handling as before
// Then create a function to perform the proper math operation and print the result as: "The result is: X" where "X" is the actual result
// If the user enters an invalid character, print: "That is not a valid operation" and then restart the program

var readLineSync = require('readline-sync'); 

console.log('What operation would you like to perform? "/", "*", "-", "+" ');
var operationSymbol = ['/', '*', '-', '+'];


var userInput = readLineSync.keyInSelect(operationSymbol);
console.log('You have selected: ' + operationSymbol[userInput]);

while (isNaN(firstNumber)) {
    console.log('Please enter the first number');
    var firstNumber = readLineSync.questionInt();
    if (isNaN(firstNumber)) {
        console.log('This is not a number');
    }
}

while (isNaN(secondNumber)) {
    console.log('Please enter the second number');
    var secondNumber = readLineSync.questionInt();
    if (isNaN(secondNumber)) {
        console.log('This is not a number');
    }
}

if (operationSymbol[userInput] === '/') {    
    var result = firstNumber / secondNumber;
    console.log('The result is: ' + result);
} else if (operationSymbol[userInput] === '*') {   
    var result = firstNumber * secondNumber;
    console.log('The result is: ' + result);
} else if (operationSymbol[userInput] === '-') {   
    var result = firstNumber - secondNumber;
    console.log('The result is: ' + result);
} else if (operationSymbol[userInput] === '+') {
    var result = firstNumber + secondNumber;
    console.log('The result is: ' + result);
}