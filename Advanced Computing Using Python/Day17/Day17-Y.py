
string1 = "ffffaaaaaaAAAAAA"

def remove_duplicates(str1):

    if str1 == "":
        raise Exception("String is empty")
    if type(str1) != str:
        raise TypeError("String is invalid")

    newString = ""
    stringchars = set(str1)

    for char in str1:
        if char in stringchars:
            if char in newString:
                continue
            else:
                newString += char

    return newString

print(remove_duplicates(string1))
