one, two, three = 0, 1, 1
while three <= 100:
    new = three + two
    one, two, three = two, three, new
    print(three)

