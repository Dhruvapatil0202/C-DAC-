

def generate_report(*args, title = "Sales report", **kwargs):
    print(f"\nTitle: {title}\n{'-' * 50}\n")

    print(f"Author: {kwargs['Author']}\n"
          f"Date: {kwargs['Date']}\n{'-' * 50}\n")

    skips = set(kwargs.get('to_skip'))
    for i in range(1, len(args) + 1):
        if i not in skips: print(f"Section {i}: {args[i-1]}")

    optional_index = 1
    for param in kwargs:
        if 'section' in param:
            print(f"{param} {optional_index}: {kwargs[param]}")
            optional_index += 1
    print("=" * 50, '\n')

    print(f"Conclusion: {kwargs['conclusion']}\n{'-' * 50}")

section1 = "Text of section 1"
section2 = "Text of section 2"
section3 = "Text of section 3"

generate_report(section1, section2, section3,
                title = "Monthly Sales Report",
                Author = "Author name",
                Date = "Date Text",
                optional_section_1 = "Text of section 4",
                optional_section_2 = "Text of section 5",
                conclusion = "Text of conclusion",
                to_skip = [2])

#--------------------------------------------------------------------------------

def generate_report(report_title, *sections,**meta_data):

    sections = list(sections)

    print(f"Enter the tuple of sections to include in your report eg-(1,3,5) Here is your list of sections: ")
    for index,section in enumerate(sections,1):
        print(f"{index}. {section}")

    choice = (int(x)-1 for x in tuple(input(f"Enter your choice here: ").split(",")))

    print("\n============================================================================")
    print(f"Report Title : {report_title.title()}")
    print("============================================================================")

    print(f"Author : {meta_data['Author']}")
    print(f"Date : {meta_data['Date']}")
    print()

    print("\n----------------------------------------------------------------------------")
    for index,include_section in enumerate(choice,1):
        print(f"Section{index}. {sections[include_section]}")
    print("----------------------------------------------------------------------------")

    print("Conclusion:")
    print("----------------------------------------------------------------------------")
    print(meta_data["conclusion"])

section1 = "Text of section 1"
section2 = "Text of section 2"
section3 = "Text of section 3"

generate_report("Monthly Sales Report", section1, section2, section3,
                Author = "Author name",
                Date = "Date Text",
                optional_section_1 = "Text of section 4",
                optional_section_2 = "Text of section 5",
                conclusion = "Text of conclusion")