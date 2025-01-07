
inp = input("Enter two numbers: ")
try:
    li = inp.split(" + ")
    sm = sum(list(map(int, li)))
    print(f"{sm}")

except Exception as e:
    print(f"Exception: {e}")

