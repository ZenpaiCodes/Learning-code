// .find()
// .findIndex()

const comments = [
  {
    id: 1,
    comment: 'Love this!',
    likes: 1500,
    user: 'joe'
  },
  {
    id: 2,
    comment: 'Super good',
    likes: 1200,
    user: 'melvin'
  },
  {
    id: 3,
    comment: 'You are the best',
    likes: 1700,
    user: 'lesly'
  },
  {
    id: 4,
    comment: 'Ramen is my fav food ever',
    likes: 800,
    user: 'jack',
  },
];

const comment = comments.find(comment => comment.likes === 800);
console.log(comment);