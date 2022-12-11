var calcBill = (total, tax = 0.0825, tip = 0.18) => { // default value for tax and tip
  totalBill = (total + (total * tax) + (total * tip));
  return totalBill;
}

console.log('Total: $' + calcBill(100, 0.13, 0.15));
