CHOICE_STR = """
1. Inches -> Feet
2. Inches -> Centimeters
3. Inches -> Meters
Type index of the choice (1, 2, 3): """

def get_choice():
    return input(CHOICE_STR)

while True:
    quit_choice = input("\nStart Distance Converter (Type y): ").lower()
    if quit_choice != "y": break

    inches_input = int(input("Enter no. of Inches to convert: "))
    choice = get_choice()

    if choice == "1":
        print(f"\n{inches_input} Inches = {inches_input * 0.083} Feet")
    elif choice == "2":
        print(f"\n{inches_input} Inches = {inches_input * 2.54} Centimeters")
    elif choice == "3":
        print(f"\n{inches_input} Inches = {inches_input * 0.0254} Meters")
    else:
        print(f"Invalid input")
