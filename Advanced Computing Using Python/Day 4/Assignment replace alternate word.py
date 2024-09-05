
paragraph = """
“The sun dipped below the horizon, casting a warm, golden glow over the tranquil lake. Birds chirped their final songs 
of the day, while the gentle breeze rustled through the leaves of the towering trees. As the sky transitioned from a 
vibrant orange to a deep indigo, the first stars began to twinkle, reflecting off the water’s surface like tiny diamonds.
 It was a moment of pure serenity, a perfect end to a beautiful day.”
"""

# list_of_paragraph = paragraph.split(" ")
#
# n = len(list_of_paragraph)
# for i in range(1, n, 2):
#     list_of_paragraph[i] = "replaced"
#
# new_paragraph = " ".join(list_of_paragraph)
# print(new_paragraph)

# __________________________________________________________________

text = input("Enter any sentence")

list_t = text.split(" ")

newText = " ".join(["replaced" if i % 2 == 1 else list_t[i] for i in range(0,len(list_t))])
print(newText)