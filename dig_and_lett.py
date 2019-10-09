""" 9. Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program:
hello world! 123
Then,
the output should be:
LETTERS 10
DIGITS 3

"""

def count(print):
    a = b = 0
    for i in print:
        if i.isalpha():
            a += 1
        elif i.isdigit():
            b += 1
        else:
            pass
    return (f'total no of digits: {b} \n total no of letters: {a}')





message = input(': ')
print(count(message))
