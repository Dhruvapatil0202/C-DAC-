
import re

text ="This is fun"
def translate(text):

    new_text = re.sub(r"[aeiouAEIOU]", "abc",text)
    print(new_text)

translate(text)