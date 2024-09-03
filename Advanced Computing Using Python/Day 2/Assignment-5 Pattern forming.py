# for i in range(1, int(input("Enter number: "))+1): print(str(i) * i)

# ________________________________________________________________________________

height = int(input("Enter the height of the pyramid: "))

for i in range(1,height+1):
    for j in range(1,i+1):
        print(i, end="")

    print("")

