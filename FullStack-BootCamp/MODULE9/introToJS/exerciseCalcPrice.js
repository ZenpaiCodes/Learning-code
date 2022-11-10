let steak = 20;
let side = 15.50;
let wine = 15;
let rice = 8;
let dessert = 5;
let tip = 15;

const coupon = .25; // 25% off
const tax = .0775; // 7.75% tax

let total = steak + side + wine + rice + dessert + tip;

// apply coupon
total = total - (total * coupon);
console.log('Total: $', total.toPrecision(4));

// apply tax
finalPrice = total + (total * tax);
console.log('Total: $', finalPrice.toPrecision(4));