function toCelsius(f) {
    var temp = (f - 32) * (5 / 9);
    return temp.toFixed(2);
} 

var cel = toCelsius(82);

var weather = "It is " + cel + " degrees Celsius outside.";

console.log(weather);




// VIDEO GAME EXAMPLE
var warrior = {
    name: "Warrior",
    level: 1,
    health: 100,
    attack: 10,
    defense: 5,
    energy: 100,
}

function levelUp(property, value) {
  warrior[property] += value;
}

levelUp("level", 1);
levelUp("health", 25);
levelUp("attack", 5);
levelUp("defense", 2);
levelUp("energy", 10);


console.log(warrior);

