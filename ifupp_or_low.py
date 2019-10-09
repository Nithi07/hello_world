"""10. Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

Suppose the following input is supplied to the program:
Hello world!
Then,
 the output should be:
UPPER CASE 1
LOWER CASE 9

"""

def count(print):
    a = b = 0
    for i in print:
        if i.isupper():
            a += 1
        elif i.islower():
            b += 1
        else:
            pass
    return (f'total no of capital letters: {a} \n total no of small letters: {b}')





message = input(': ')
print(count(message))