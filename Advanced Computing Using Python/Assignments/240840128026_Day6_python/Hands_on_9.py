import re

SAMPLE_TEXT = """
Hello Team,

Please find the contact details for the project stakeholders below:

Alice Johnson: +1-800-555-1234
Bob Smith: (123) 456-7890
Carol Lee: 123.456.7890
David Brown: 123-456-7890
Eve Martinez: +44 20 7946 0958
Frank Wright: +1 (800) 555-9876
Grace Lee: 800-555-5555
Henry O'Neil: +61 2 9876 5432
Irene Gomez: 1234567890
Jack Black: 123 456 7890
Best regards,

Project Coordinator
+1-800-123-4567
"""

if __name__ == "__main__":
    string_list = SAMPLE_TEXT.split("\n")

    regular_expression = r"\(\d{3}\) \d{3}\-\d{4}"
    for text in string_list:
        out_li = re.findall(pattern = regular_expression, string= text)
        if out_li:
            print(out_li)
    