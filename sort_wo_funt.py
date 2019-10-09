""" 10. (2) Write a python program to sort a given list of numbers with out using sort() function

"""
a = [6,90,4,2]
b = []
for i in range(len(a)):
    c = min(a)
    b.append(c)
    a.remove(c)
print(b)