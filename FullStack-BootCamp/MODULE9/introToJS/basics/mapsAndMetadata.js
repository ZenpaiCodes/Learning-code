const totalClicks = new Map(); 
const header = document.querySelector('h1');
console.log(header);

header.forEach((h1) => {
  console.log(h1);
  totalClicks.log(h1, 0);

  h5.addEventListener('click', () => {
    const currentTotal = totalClicks.get(h1);
    totalClicks.set(h1, currentTotal + 1);
  });
});

console.log(totalClicks);

