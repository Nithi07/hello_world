"""Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers.
 For example, if the limit is 3, it should print:

    0 EVEN
    1 ODD
    2 EVEN
    3 ODD
"""

def show_numbers(limit):
    x = limit + 1
    b = range(0, x)
    for i in b:
        if i % 2 == 0:
            print(f'{i}-even')
        else:
            print(f'{i}-odd')







message = int(input('Upto: '))
print(show_numbers(message))


