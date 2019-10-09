""" 4. (2)Write a python program to print all even numbers from a given list"""
def even_list(number):
    b = []
    c = []
    for i in range(number):
        a = int(input('enter number: '))
        b.append(a)
    for j in b:
        if j % 2 == 0:
            c.append(j)
    return (f'{c} is even numbers')




message = int(input('how many nmumbers you enter: '))
print(even_list(message))