"""Write a function called show_stars(rows). If rows is 5, it should print the following:

    *
    **
    ***
    ****
    *****
"""


def show_stars(rows):
    i = rows + 1
    x = range(0, i)
    for star in x:
        y = star * '*'
        print(y)



message = int(input('enter you limit: '))
print(show_stars(message))