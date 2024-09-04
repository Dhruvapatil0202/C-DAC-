
# students_num = int(input("Enter number of students: "))
#
# students_info = []
# for _ in range(students_num):
#     name = input("Name: ")
#     age = int(input("Age: "))
#     score1 = float(input("Score1: "))
#     score2 = float(input("Score2: "))
#     score3 = float(input("Score3: "))
#     print("")
#
#     average = round((score1 + score2 + score3) / 3, 3)
#
#     students_info.append((name, age, score1, score2, score3, average))
#
# students_info.sort(key = lambda x: x[5], reverse = True)
#
# print(f"Student with Highest avg. score is {students_info[0][0]} with avg. score of {students_info[0][-1]}")
#
# avg_score_limit = float(input("Enter limit of avg. score: "))
#
# print("\nStudents satisfying criteria are: \n")
# for name, age, s1, s2, s3, avg_score in students_info:
#     if avg_score >= avg_score_limit:
#         print(f"{name} scoring {avg_score}")

#_________________________________________________________________________________________

student_data = []
updated_student_data = []
highest_score = 0

strength = int(input("Enter the strength of the students: "))

while strength > 0:
    student_data.append(tuple(input("Enter the data of the student in format: (Name, Age, Score1, Score2, Score3): ").split(",")))
    strength-=1

student_with_highest_score = None
highest_score = 0
for index,student in enumerate(student_data):
    name,age,score1,score2,score3 = student
    avg_marks = (int(score1) + int(score2) + int(score3))/3
    stud_info = (name,age,score1,score2,score3,avg_marks)
    updated_student_data.append(stud_info)
    if avg_marks > highest_score:
        student_with_highest_score = stud_info
        highest_score = avg_marks

print("\n------------------------------------------------------")
print(f"Student with highest average score: {student_with_highest_score[0]} : {highest_score}")
print("\n------------------------------------------------------")

min_avg_score = int(input(f"Enter the minimum average score to sort the student data accordingly: "))

print("\n------------------------------------------------------")
ind = 1
for student in updated_student_data:
    if int(student[-1]) >= min_avg_score:
        print(f"{ind}. {student[0]} : {student[-1]}")
        ind +=1
print("\n------------------------------------------------------")

