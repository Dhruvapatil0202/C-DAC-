

pyra_height = int(input("Enter height of the pyramid: "))

for lvl in range(pyra_height  + 1):
    print(f"{' '*(pyra_height - lvl)}{'*' * (( 2 * lvl) - 1)}")


