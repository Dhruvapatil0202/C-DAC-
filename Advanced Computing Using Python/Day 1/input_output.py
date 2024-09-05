# Regular Input - output
var_1 = input("enter var_1: ")
var_2 = input("enter var_2: ")

print("var_1 is {}, var_2 is {}".format(var_1, var_2))
print("var_1 is {1}, var_2 is {0}".format(var_1, var_2))
print("var_1 is {v1}, var_2 is {v2}".format(v1 = var_1, v2 = var_2))


# using f-string
print(f"var_1 is {var_1}, var_2 is {var_2}")

# Seperators
print("hello", "world", sep = " ")
print("hello", "world", sep = " - ")
print("hello", "world", sep = ", ")

# End
print("Line 1", end = "\n\t")
print("Line 2")
