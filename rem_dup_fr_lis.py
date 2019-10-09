""" 6. (2)Write a python program to remove repeated elements from a given list without using built-in methods"""

def rem_dup(list):
    b = []
    for i in list:
        if i not in b:
            b.append(i)
    return b

print(rem_dup([2,4,89,4]))

