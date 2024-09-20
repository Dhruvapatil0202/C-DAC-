# Assignment : removing duplicate character  keeping first occurrence of each character

string_cand = "akdoiwenEMVWEogiwnoiengoWEGOIWEFOwineoinfoiWEFAJEWIWJOGawneogihweiWOEOIWNEGOohnvo"

def remove_duplicate_characters(string_inp: str):
    if type(string_inp)  != str:
        raise TypeError('The input is not string')
    elif not string_inp:
        raise Exception("Entered the empty string")
    output, st = "", set()
    for char in string_inp:
        if char in st: continue
        output += char
        st.add(char)

    return output


out_str = remove_duplicate_characters(string_cand)
# out_str = remove_duplicate_characters(5)
# out_str = remove_duplicate_characters("")
print(out_str)




