"""1.(2) Write a python program to find the sum of all numbers in a list"""
def sum_list(numbers):
    a = range(numbers)
    c = []
    for _ in a:
        b = int(input('enter your number: '))
        c.append(b)
    return sum(c)






message = int(input('how many numbers you calculate: '))
print(sum_list(message))