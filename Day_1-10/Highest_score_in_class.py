student_scores = input("Input a list of student scores ").split() # 1st split each answer into an individual piece of data
for n in range(0, len(student_scores)): # loop each number
  student_scores[n] = int(student_scores[n]) # turn each piece of data into an integer
print(student_scores) # see list

student_scores.sort() # sort the list smallest to biggest
print(f"The highest score in the class is: {student_scores[-1]}") # print last piece of data after sorted


# OPTIONAL SOLUTION
# highest_score = 0
# for score in student_scores:
#   if score > highest_score:
#     highest_score = score
# print(highest_score)