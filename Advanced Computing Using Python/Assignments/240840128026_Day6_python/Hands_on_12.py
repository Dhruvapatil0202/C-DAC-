"""
Regular expression for extracting valid IP addresses from text.
"""
import re

SAMPLE_TEXT = """
192.168.1.1
255.255.255.255
0.0.0.0
123.456.78.90
10.0.0.1
172.16.254.1
300.200.100.50
192.168.0.256
192.168.1.
192.168..1
192.168.1.300
172.16.0.1
192.168.1.999
192.168.1.1000
999.999.999.999
192.168.1.1.1
192.168.1.1a
192.168.1.a1
192.168.1.1.
.192.168.1.1
192.168.1..1
256.256.256.256
192.168.0.0
8.8.8.8
127.0.0.1
192.168.1.255
169.254.0.1
198.51.100.0
203.0.113.0
192.0.2.0
233.252.0.0
192.168.100.100
100.100.100.100
192.168.10.10
200.200.200.200
250.250.250.250
1.1.1.1
192.168.1.300
192.168.1.257
123.456.78.90
192.168.1.0.1
192.168.1.0.
192.168.01.1
010.0.0.1
10.0.0.01
10.0.0.0.1
0.10.0.0
10.0.0.10
10.0.10.0
10.10.0.0
192.168.1.10
10.0.0.256
256.0.0.0
0.0.0.256
256.256.256.256
192.168.1.256
1.1.1.256
1.256.1.1
256.1.1.1
192.168.1.1
10.0.0.2
172.16.254.2
192.168.2.1
100.64.0.1
192.0.0.1
224.0.0.1
240.0.0.1
169.254.1.1
203.0.113.1
198.51.100.1
192.0.2.1
192.168.1.256
172.16.0.256
10.0.0.256
192.168.0.257
127.0.0.257
192.168.1.1
8.8.8.8
8.8.4.4
8.8.8.8.8
192.168.1.1
1.1.1.1
1.1.1.300
300.1.1.1
1.300.1.1
1.1.300.1
1.1.1.300
192.168.1.1
10.0.0.1
172.16.254.1
100.64.0.1
192.0.0.1
224.0.0.1
240.0.0.1
169.254.1.1
203.0.113.1
198.51.100.1
192.0.2.1
0.0.0.0
255.255.255.255
"""

if __name__ == "__main__":
    text_list = SAMPLE_TEXT.split("\n")
    expression = r"((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])"
    for text in text_list:
        out = re.match(pattern= expression, string= text)
        if out:
            print(out.group())

    



    