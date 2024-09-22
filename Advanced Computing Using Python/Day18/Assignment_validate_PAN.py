import re
text = """
In today’s financial workshop, we discussed various important documents. For instance, John shared his PAN number, 
which is ABCDE1295E. Meanwhile, Sarah mentioned hers as FGHIJ1455H, while Mike chimed in with JKLMN1265P.

As we explored investment options, I noted down a few more, including OPQRS1855T. Everyone seemed impressed with the 
potential returns. To conclude, we highlighted the need for compliance, reminding participants to keep their records 
straight, such as QRSTU1214W.
"""

pat = r"\b(?:[A-Z]{5}\d{4}[A-Z][^a-z]?)\b"

print(re.findall(pat, text))