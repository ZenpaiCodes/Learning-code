// Build your own promises from scratch
const promise = new Promise((resolve, reject) => {
  setTimeout(() => { 
    resolve({}); 
  }, 2000); // 2 seconds before loading the data
    if (true) {
        resolve('Stuff Worked! ✔');
    } else {
        reject('Error, it broke 😢');
    }
});

promise
    .then((data) => console.log(data))
    .catch((err) => console.log(err, 'No data!'));