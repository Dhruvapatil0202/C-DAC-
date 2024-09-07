
import re
cand_text = ['invalid-gmail@com', 'sample@gmail.com', '2inval#id%@gmail.com']
pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
for mail in cand_text:
    out = re.fullmatch(pattern, mail)

    # if out:
    #     print("\n\n", out.__dict__, "\n\n")
    print(f"{mail} - {out.group() == mail if out else False}")

