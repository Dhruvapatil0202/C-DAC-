
# # text = input("Input any text: ")
# text = "Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"
# code = {"a": "n", "b": "o", "c": "p", "d": "q", "e": "r", "f": "s", "g": "t", "h": "u", "i": "v", "j": "w", "k": "x", "l": "y", "m": "z", "n": "a", "o": "b", "p": "c", "q": "d", "r": "e", "s": "f", "t": "g", "u": "h", "v": "i", "w": "j", "x": "k", "y": "l", "z": "m", "A": "N", "B": "O", "C": "P", "D": "Q", "E": "R", "F": "S", "G": "T", "H": "U", "I": "V", "J": "W", "K": "X", "L": "Y", "M": "Z", "N": "A", "O": "B", "P": "C", "Q": "D", "R": "E", "S": "F", "T": "G", "U": "H", "V": "I", "W": "J", "X": "K", "Y": "L", "Z": "M"}
# #
# # def get_char(character):
# #     char_ind = ord(character)- ord('a') +1
# #     if (char_ind + 13) > 26:
# #         return chr(ord('a') + ((char_ind+13) % 26))
# #     else:
# #         return chr(char_ind+13)
#
# # char_dict = {char : get_char(char) for char in text}
# # print(char_dict)
#
#
# def encode(text):
#     encoded = ""
#     # for character in text:
#     #     if character == " ":
#     #         encoded+=" "
#     #     else:
#     #         encoded+= code[character]
#     #
#     # return encoded
#     for char in text:
#         if char in code:
#             encoded += code[char]
#         else:
#             encoded += char
#     return encoded
#
# encoded = encode(text)
# decoded = encode(encoded)
# print(f"Encoded : {encoded}")
# print(f"Decoded: {decoded}")


# text = "Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"
# def get_char(character):
#     if character.isupper(): piv = 'A'
#     else: piv = 'a'
#
#     char_ind = ord(character) - ord(piv)
#     if char_ind + 13 <= 26:
#         return chr(ord(piv) + char_ind + 13)
#     else:
#         return chr(ord(piv) + char_ind - 13)
#
# char_dict = {char : get_char(char) for char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"}
#
# encod_text = [get_char(char) for char in text if char in char_dict]
# print(encod_text)