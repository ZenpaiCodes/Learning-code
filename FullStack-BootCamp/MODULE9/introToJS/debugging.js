/*
Directions:
1. Fix syntax errors.
2. Run the following code as-is and read the error message.
3. Fix the mistake, and then re-run the code to check it.
Expected Output:
=> WARNING: Insufficient energy!
*/

let readyToSkate = false;
let energyLevel = 18000;

/* if (energyLevel >= 24000 {
  console.log("Energy level is a go!");
  readyToSkate = true; */
if (energyLevel >= 24000) {
   console.log("Energy level is a go!");
   readyToSkate = true;
} else {
   console.log("WARNING: Insufficient energy!");
   readyToSkate = false;
}

// EXERCISE -2 
/*
Directions:
1. The block of code has a few syntax errors.
2. Run the code as-is to find the mistakes.
💡 Tip:
Only one error will be flagged at a time.
Fix that ONE problem, and then re-run the code to check your work.
Avoid trying to fix multiple issues at once.
Expected Output:
=> Crew & cameraBattery is a go!
=> Grab your skateboard...
=> Ready...
=> Set...
=> SKATE!
*/

let readySkate = false;
let crewStatus = true;
let cameraBattery = "green";

if (crewStatus && cameraBattery == "green") {
   console.log("Crew & cameraBattery is a go!");
   readySkate = true;
} else {
   console.log("WARNING: Crew or cameraBattery not ready!");
   readySkate = false;
}

if (readySkate) {
   console.log("Grab your skateboard...");
   console.log(("Ready..."));
   console.log("Set...");
   console.log("SKATE!");
} else {
   console.log("No skating today.")};

   