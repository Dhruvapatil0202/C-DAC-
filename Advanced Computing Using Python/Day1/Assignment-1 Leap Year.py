
year = int(input("Enter the Year: "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0: print(f"{year} is a Leap year")
#         else: print(f"{year} is not a Leap year")
#     else: print(f"{year} is a Leap year")
# else: print(f"{year} is not Leap year")


#------------------------------------------------------------------

# if (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 400 == 0):
#     print("Leap")
# else: print("Not Leap")

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a Leap year")
else: print(f"{year} is not a Leap year")


# if year % 4 == 0 or year % 400 == 0:
#     print(f"{year} is a Leap year")
# else: print(f"{year} is not a Leap year")