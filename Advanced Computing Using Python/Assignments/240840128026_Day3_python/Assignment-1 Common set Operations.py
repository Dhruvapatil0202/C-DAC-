
mathe_studs = {"Alice", "Bob", "Charlie", "David"}
science_studs= {"Charlie", "David", "Eve", "Frank"}

# Students Enrolled in both Math and Science
print(f"Students Enrolled in both Math and Science: {sorted(mathe_studs.intersection(science_studs))}")

# Students Enrolled in Math but not in Science
print(f"Students Enrolled in Math but not in Science: {sorted(mathe_studs - science_studs)}")

# Students Enrolled in Math, Science or Both
print(f"Students Enrolled in Math, Science or Both: {sorted(mathe_studs.union(science_studs))}")

# Students Enrolled in Science but not in Math
print(f"Students Enrolled in Science but not in Math: {sorted(science_studs - mathe_studs)}")
