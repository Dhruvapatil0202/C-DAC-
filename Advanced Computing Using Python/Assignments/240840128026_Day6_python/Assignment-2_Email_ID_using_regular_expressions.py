import re

# All emails in SAMPLE_TEXT are valid emails.
SAMPLE_TEXT = """Hello Team,

Please find the contact details for the project stakeholders below:

Alice Johnson - alice.johnson@example.com
Bob Smith - bob_smith123@company.org
Carol Lee - carol.lee@work-email.net
David Brown - david_brown@domain.co.uk
Eve Martinez - evemartinez@service.biz
Best regards,

Project Coordinator
project.coordinator@example.org

"""

if __name__ == "__main__":

    list_of_lines = SAMPLE_TEXT.split("\n")

    regex = r"[\w\.]+@[\w\-]+[_a-z]{2,5}\.[a-z\.]{1,8}"
    reg = r"[\w\.]+@[\w\-]+\.[\.a-z]{1,7}"

    print("\n")
    for text in list_of_lines:
        result = re.findall(pattern = reg, string = text)
        if result: 
            print(result)
    print("\n")


