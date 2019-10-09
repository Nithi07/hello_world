""" `1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
"""

def sum(number):
    key = []
    for res in number:
        if (not res % 5 == 0) and res % 7 == 0:
            key.append(res)
    return key




print(sum(range(2000, 3201)))