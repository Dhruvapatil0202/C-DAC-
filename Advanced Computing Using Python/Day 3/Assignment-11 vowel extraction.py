
# print([i for i in input("Enter the string here: ").lower() if i in "aeiou"])

#-------------------------------------------------------------------------------

text = input("Enter the text: ")
vowels = [vowel for vowel in text if vowel.lower() in "aeiou"]
print(vowels)