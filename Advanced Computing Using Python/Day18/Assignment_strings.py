


scores = input("Enter the list of grades seperated by commas: ").split(",")

try:
    int_grades = [int(score) for score in scores]
    print(int_grades)
except ValueError:
    print("Values you entered cannot be converted")

