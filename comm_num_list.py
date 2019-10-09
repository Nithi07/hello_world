""" 3. (2)Write a python program to find the common numbers from two lists"""

def common_numbers():
    a = [3,6,80,1,8]
    b = [6,8,7]
    c = []
    for i in a:
        for j in b:
            if i == j:
                c.append(i)
    return f'{c} :is common num of two lists'



print(common_numbers())
