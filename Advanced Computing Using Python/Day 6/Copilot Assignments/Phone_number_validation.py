import re
texts = ["(123) 456 7890", "(987) 654-3210", "9856509847"]
pattern = r"\(\d{3}\) \d{3} \d{4}"
for num in texts:
    mth = re.match(pattern, num)
    if not mth:
        print(f"{num} is not a valid number")
    else:
        print(f"{mth.group()} is a valid number")

