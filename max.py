""" 2. (2)Write a python program to find largest number in a given list with out using max()"""
a = int(input('how many numbers you enter: '))
b = range(a)
d = []
for i in b:
    c = int(input('enter your number: '))
    d.append(c)
    e = d[0]
    for j in d:
        if j > e:
            e = j
    print(e)