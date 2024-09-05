
paragraph = """ The sun dipped below the horizon, casting a warm, golden glow over the tranquil lake. Birds chirped their final songs of the day, while the gentle breeze rustled through the leaves of the towering trees. As the sky transitioned from a vibrant orange to a deep indigo, the first stars began to twinkle, reflecting off the water’s surface like tiny diamonds. It was a moment of pure serenity, a perfect end to a beautiful day. """

split_words = paragraph.split(" ")

sorted_words = list(sorted(set(split_words)))

print(sorted_words)
