let classRoom = {
  grade: '3rd drade',
  students: [
    { name: 'John', score: 90 },
    { name: 'Jane', score: 80 },
    { name: 'Mark', score: 100 },
    { name: 'Mary', score: 85 },
  ]
}

let starStudents = classRoom.students
  .filter(function(student) {
    return student.score > 80;
  })
  .map(function(value) {
    value.score += 5;
    return value;
  })
  .reduce(function(acc, val, i, array) {
    const total = acc.sum + val.score;
    return {
      sum: total,
      arr: array,
    }
  }, {sum: 0, arr: []});

  let studentAverage = starStudents.sum / starStudents.arr.length;

console.log(starStudents, studentAverage);