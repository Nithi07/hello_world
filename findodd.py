def find_odd(a):
    key = []
    for i in a:
        if i % 2 == 1:
            key.append(i)
    return (key)

print(find_odd(range(21)))
