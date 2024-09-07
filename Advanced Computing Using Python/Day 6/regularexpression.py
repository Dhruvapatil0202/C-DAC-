
# import re
#
# pattern = r'\d+'
# text = 'There are 123 435 apples'
# li = re.findall(pattern, text)
# if li:
#     print('Found: ', li)

"""
regular expression functions:
1. re.findall() : Returns list of all matches
2. re.search(): search for first match and return a match
3. re.split(): splits the string by the occurrences of pattern
4. re.sub(): replaces one or many matches with a string.

"""

import re

text = 'contact us at support@example.com or sales@example.com'
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

emails = re.findall(pattern, text)
print(emails)