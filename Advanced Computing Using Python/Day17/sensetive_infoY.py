

import re

email = "abcd.xyz@gmail.com"
credit = "1234 5678 9101 1213"


def mask_sensetive_info(info, info_type):

    if info_type == "email":

        masked_email = re.sub(r"\b(^\w)([a-zA-Z\d\.\_]*)(\w@)\b", r"\1***\3", info)
        print(masked_email)

    else:
        masked_credit = re.sub(r"\b(\d{4} \d{4} \d{4}) (\d{4})\b",r"**** **** **** \2", info)
        print(masked_credit)

mask_sensetive_info(credit,"credit")

