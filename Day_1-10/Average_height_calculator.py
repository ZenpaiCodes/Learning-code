student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for total in student_heights:
    total_height += total   # acting as a sum() to add all the heights data

students_num = 0
for total_students in student_heights:
  students_num += 1    # acting as a len() to find out how many students to devide for

average_height = round(total_height / students_num)   # all heights devided by number of students to find average
print(average_height)
