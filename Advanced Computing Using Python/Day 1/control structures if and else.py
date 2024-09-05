score = 80
attendance = 98

if score >= 90:
    if attendance >= 90:
        print(f"Grade: A+, Honors")
    else:
        print(f"Grade: A")

elif score >= 75:
    if attendance >= 90:
        print(f"Grade B+, Good")
    else:
        print(f"Grade B")

else:
    print("Grade C")

