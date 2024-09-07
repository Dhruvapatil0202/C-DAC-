
import re

# with open('re_practice.txt', 'r') as file:
#     cands = file.readlines()
#
#
# pattern = r'^start.*end.$'
#
# for text in cands:
#     text = text.replace('\n', '').strip()
#     out = re.match(pattern, text)
#     print(f"{text} -> {True if out else False}")


with open ("re_practice.txt", 'r') as file:

    for line in file.readlines():
        if re.match(r'^start.*end.$',line.replace("\n","").strip()):
            print(line)
