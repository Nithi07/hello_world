"""
Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter).
For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.
"""

def sum (limit):
    i = limit + 1
    x = range(0, i)
    res = []
    for num in x:
        if num % 3 == 0 or num % 5 == 0:
            res.append(num)
    return res





message = int(input('upto: '))
print(sum(message))