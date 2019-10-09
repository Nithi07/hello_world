"""5. (2)Write a python program to create a list of even numbers and another list of odd numbers from a given list
"""
def even_list(number):
    b = []
    c = []
    d = []
    for i in range(number):
        if i == i:
            a = int(input('enter number: '))
            b.append(a)
    for j in b:
        if j % 2 == 0:
            c.append(j)
        else:
            d.append(j)
    print(f'{c}even number/s')
    print(f'{d}odd number/s')



message = int(input('how many nmumbers you enter: '))
print(even_list(message))