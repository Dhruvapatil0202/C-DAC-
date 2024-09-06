
import sys

# def get_text_from_file(filename):
#     try:
#         with open(filename, 'r') as file:
#             out_text = file.read()
#     except FileNotFoundError:
#         print("The required file does not exist. 1")
#         sys.exit()
#     # print(out_text)
#     return out_text
#
#
# def write_text_to_file(filename, text):
#     try:
#         with open(filename, 'w') as file:
#             file.write(text)
#     except FileNotFoundError:
#         print("The required file does not exist. 2")
#         sys.exit()
#     finally:
#         return
# def replace_word(filename, target_word, new_word):
#
#     text = get_text_from_file(filename)
#
#     text = text.replace(target_word, new_word)
#
#     write_text_to_file(filename, text)
#
#     pass
#
#
# if __name__ == "__main__":
#
#     replace_word('Report', 'section', 'temp')

# ___________________________________________________________________

def readFile(file_name):

    try:
        with open(file_name,'r') as file:
            text = file.read(file_name)
        return text
    except FileNotFoundError:
        print(f"File with file name {file_name} does not exist")
        sys.exit()

def writeFile(file_name):
    pass


def replaceWord(file_name, old_word, new_word):
    pass

