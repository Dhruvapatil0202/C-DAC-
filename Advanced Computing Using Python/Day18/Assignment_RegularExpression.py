
import re
file_path = r"C:\Users\DAI.STUDENTSDC\Desktop\DAI 2024\Day18\temp_records.csv"

with open(file_path) as file:
    lines = file.readlines()

print(lines)
regex = r"\bdatetime=(\d{4}\-\d{2}\-\d{2})T(\d{2}:\d{2}:\d{2})\b"
new_format = r"date=\1#time=\2"

new_lines = []
for line in lines:

    new_lines.append(re.sub(regex, new_format, line))
    # print(re.findall(regex, line))
print(new_lines)

with open("temp_record_modified.csv", mode= 'w') as file:
    file.writelines(new_lines)