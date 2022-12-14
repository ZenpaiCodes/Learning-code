// Classes and using Super()
class User {
  constructor(username, email) {
    this.username = username;
    this.email = email;
    this.hobbies = [];
  }

  greeting() {
    console.log(`Hi, ${this.username} today is your day!`);
  }

  addHobby(hobby) {
    this.hobbies.push(hobby);
    return this.hobbies;
  }
};

class Admin extends User {
  constructor(username, email, title, exclusiveAccess) {
    super(username, email);
    this.title = title;
    this.exclusiveAccess = exclusiveAccess;
  }

  createUser(name) {
    console.log(`Creating new user ${name}...`)
  }
};

const user1 = new User('John', 30);
console.log(user1.greeting()); // hobbies is empty at this point. add below ⤵ 

user1.addHobby('Soccer');
user1.addHobby('Basketball');
console.log(user1.hobbies);

const admin1 = new Admin('Jane', 'admin@email.com', 'administrator', true);
console.table(admin1);

admin1.addHobby('Gaming, boxing');
console.table(admin1);

