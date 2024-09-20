
# days = int(input("Enter the days in a month: "))
#
# weekday = int(input("Enter the day of the week: "))
#
# def calender_month(days, weekday):
#     calender = [
#         "sun",
#         "mon",
#         "tue",
#         "wed",
#         "thu",
#         "fri",
#         "sat"
#     ]
#     weekday %= 7
#     print("  ".join(calender))
#
#     grid = []
#     temp = ["     " for _ in range(weekday)]
#
#     for i in range(1, days + 1):
#         if temp and len(temp) % 7 == 0:
#             grid.append(temp)
#             temp = []
#         if i <= 9: temp.append(str(i) + "    ")
#         else: temp.append(str(i) + "   ")
#
#     grid.append(temp)
#
#     for line in grid:
#         print("".join(line))
#
# calender_month(54, 3)


#------------------------------------------------------------------------------

days = int(input("Enter the days in a month: "))

weekday = int(input("Enter the day of the week: "))

def calender_day(days, weekday):
    calender = [
        "sun",
        "mon",
        "tue",
        "wed",
        "thu",
        "fri",
        "sat"
    ]

    for day in calender:
        print(f"{day} ", end="\t")


    dates = [date for date in range(1,days+1)]
    while weekday>0:
        dates.insert(0," ")
        weekday-=1
    print()
    current_day = 0
    for date in dates:
        print(date, end="\t\t")
        current_day=(current_day%7)+1
        if current_day ==7:
            print()



calender_day(days, weekday)
