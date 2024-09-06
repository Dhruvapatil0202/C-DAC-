
temps = {'1': 'Celsius',
         '2': 'Fahrenheit',
         '3': 'Kelvin'}

temp_choice = """
1. Celsius
2. Fahrenheit
3. Kelvin
Enter your choice: """

temp_choice_2 = """
1. Celsius
2. Fahrenheit
3. Kelvin
Enter your choice: """

def kelvin_to_others(target, magnitude):
    match target:
        case "2":
            return ((magnitude - 273.15) * 9/5) + 32
        case "1":
            return magnitude - 273.15

def fahranheit_to_others(target, magnitude):
    match target:
        case "1":
            return (magnitude - 32) * 5/9
        case "3":
            return ((magnitude - 32) * 5/9) + 273.15

def celsius_to_others(target, magnitude):
    match target:
        case "2":
            return (magnitude * 9 / 5) + 32
        case "3":
            return magnitude + 273.15
def convert(source, target, magnitude):
    if source == target: return magnitude

    out = None
    match source:
        case "1": out = celsius_to_others(target, magnitude)
        case "2": out = fahranheit_to_others(target, magnitude)
        case "3": out = kelvin_to_others(target, magnitude)

    return out

while True:

    user_temp_type = 'x'
    while user_temp_type not in "123":
        user_temp_type = input(temp_choice)
        if user_temp_type not in "123":
            print("Invalid Input")

    while True:
        user_temp_magnitude = input(f"Enter Magnitude of temperature: ").strip()
        try:
            user_temp_magnitude = float(user_temp_magnitude)
        except TypeError:
            print("Invalid Input\n")
        else: break

    target_unit = 'x'
    while target_unit not in "123":
        target_unit = input(temp_choice_2)
        if target_unit not in "123":
            print("Invalid Input")

    new_magnitude = convert(user_temp_type, target_unit, user_temp_magnitude)
    print(f"{user_temp_magnitude} {temps[user_temp_type]} = {new_magnitude} {temps[target_unit]}")
    exit_inp = 'x'
    while exit_inp not in 'yn':
        exit_inp = input("Do you want to exit? Y/N").lower()
        if exit_inp not in "yn": print("Invalid Input")
    if exit_inp == 'y': break


