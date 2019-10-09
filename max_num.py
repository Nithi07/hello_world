def max_num(number):
    key = []
    key[0:-1] = [number]
    max = key[0]
    for x in key:
        if x > max:
            max = x
    return max

message = (input('enter the numbers:  '))
print(max_num(message))