import re

inp_string = """
Email: Mayura.kumari@xyz.com
Credit_card: 1234 5214 1254 6325
"""

def mask_sensitive_info(input_string, infotype):
    if type(input_string) != str:
        raise TypeError("input_string is not string")

    if type(infotype) != str:
        raise TypeError("infotype is not a string")

    if infotype not in "email credit_card":
        raise ValueError("infotype is invalid: it can only be \'email\' or \'credit_card\'")

    if not infotype or not input_string:
        raise ValueError(f"Empty strings are not valid as inputs: infotype = {infotype}, input_string = {input_string}")

    if infotype == "email":
        line_list = input_string.split("\n")
        for l_ind in range(len(line_list)):
            line = line_list[l_ind]
            words = line.split(" ")
            for w_ind in range(len(words)):
                word = words[w_ind]
                if "@" in word:
                    parts = word.split("@")
                    first_part = parts[0][0] + "***" + parts[0][-1]
                    second_part = parts[1]
                    words[w_ind] = first_part + "@" + second_part

                else: continue
            line_list[l_ind] = " ".join(words)
        return "\n".join(line_list)


    elif infotype == "credit_card":
        regex = r"\d{4} \d{4} \d{4} \d{4}"

        lines = input_string.split("\n")
        for l_ind in range(len(lines)):
            line = lines[l_ind]
            match = re.findall(pattern = regex, string= line)
            if match:
                pat = match[0]
                last_four = pat[-4:]
                ret_pat = "**** **** ****" + last_four
                line = lines[l_ind]
                lines[l_ind] = line.replace(pat, ret_pat)

        return "\n".join(lines)

    else: raise Exception("Unknown Error")

# print(mask_sensitive_info(inp_string, "email"))
print(mask_sensitive_info("", 'email'))