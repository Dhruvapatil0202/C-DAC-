
# def generate_report(*args, title = "Sales report", **kwargs):
#     out = ""
#     out += f"\nTitle: {title}\n{'-' * 50}\n"
#
#     out += f"Author: {kwargs['Author']}\nDate: {kwargs['Date']}\n{'-' * 50}\n"
#
#     skips = set(kwargs.get('to_skip'))
#     for i in range(1, len(args) + 1):
#         if i not in skips: out += f"Section {i}: {args[i-1]}\n"
#
#     optional_index = 1
#     for param in kwargs:
#         if 'section' in param:
#             out += f"{param} {optional_index}: {kwargs[param]}\n"
#             optional_index += 1
#     out += "=" * 50 + '\n'
#
#     out += f"Conclusion: {kwargs['conclusion']}\n{'-' * 50}"
#     return out
#
# section1 = "Text of section 1"
# section2 = "Text of section 2"
# section3 = "Text of section 3"
#
# report = generate_report(section1, section2, section3,
#                 title = "Monthly Sales Report",
#                 Author = "Author name",
#                 Date = "Date Text",
#                 optional_section_1 = "Text of section 4",
#                 optional_section_2 = "Text of section 5",
#                 conclusion = "Text of conclusion",
#                 to_skip = [2])
#
# try:
#     with open("ass2_file1", mode = 'w') as file:
#         file.write(report)
# except Exception as error:
#     print(f"{error} Error occurred in program")

#___________________________________________________________________________________________

def generate_report(report_title, *sections,**meta_data):

    sections = list(sections)

    print("Enter the tuple of sections to include in your report eg-(1,3,5) Here is your list of sections: ")
    for index,section in enumerate(sections,1):
        print(f"{index}. {section}")

    choice = (int(x)-1 for x in tuple(input(f"Enter your choice here: ").split(",")))

    text = "\n============================================================================"
    text += f"\nReport Title : {report_title.title()}"
    text += "\n============================================================================"

    text += f"\nAuthor : {meta_data['Author']}"
    text += f"\nDate : {meta_data['Date']}"
    text += "\n"

    text += "\n----------------------------------------------------------------------------"
    for index,include_section in enumerate(choice,1):
        text += f"\nSection{index}. {sections[include_section]}"
    text += "\n----------------------------------------------------------------------------"

    text += "\nConclusion:"
    text += f'{meta_data["conclusion"]}'
    text += "\n----------------------------------------------------------------------------"
    return text

section1 = "Text of section 1"
section2 = "Text of section 2"
section3 = "Text of section 3"

def saveReport(file_name,text):

    with open(file_name,'w') as file:
        file.write(text)
    print(f"Data saved in {file_name} successfully!")

saveReport("Report", generate_report("Monthly Sales Report", section1, section2, section3,
                Author = "Author name",
                Date = "Date Text",
                optional_section_1 = "Text of section 4",
                optional_section_2 = "Text of section 5",
                conclusion = "Text of conclusion"))


def readFile(filename):
    try:
        with open(filename,'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"The file named {filename} does not exist.")

readFile("Report")