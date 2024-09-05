
dictionary = {"Alice" : 60,
              "Bob" : 93,
              "Frank" : 80,
              "Norman" : 79}

# modifying dictionary, keeping records only for students with score equal or more than 80 and increaseing it by 5

dictionary = {stud : score + 5 for stud, score in dictionary.items() if score >= 80}

print(dictionary)