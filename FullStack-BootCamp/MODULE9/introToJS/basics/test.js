function* backupGenerator() {
    let x = 0;
    for (let i = 0; i < 10; i += 1) {
      yield x += 1;
    }
  }
 
  const gen = backupGenerator();
  gen.next();
  console.log(gen.next().value); // What will be printed here?