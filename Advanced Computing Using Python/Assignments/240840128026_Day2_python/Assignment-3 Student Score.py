

student_name = input("Enter student name: ")
homework_score = float(input(f"Enter Homework score of {student_name} (out of 100): "))
quiz_score = float(input(f"Enter Quiz score of {student_name} (out of 100): "))
mid_term_score = float(input(f"Enter Mid term score of {student_name} (out of 100): "))
final_score = float(input(f"Enter final exam score of {student_name} (out of 100): "))

if not 0 <= homework_score <= 100 or not 0 <= quiz_score <= 100 or not 0 <= mid_term_score <= 100 or not 0 <= final_score <= 100:
    print("Invalid Score")

else:
    total_score = homework_score * 0.2 + quiz_score * 0.2 + mid_term_score * 0.3 + final_score * 0.3
    total_score_percent = (total_score * 100) / 100

    if total_score_percent > 90: grade = "A"
    elif 75 <= total_score_percent < 90: grade = "B"
    elif 60 <= total_score_percent < 75: grade = "C"
    elif 45 <= total_score_percent < 60: grade = "D"
    else: grade = "E"

    print(f"\nFinal score of {student_name} is {total_score_percent}% with grade \"{grade}\".")