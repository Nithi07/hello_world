def prime_number():
    message = int(input('enter your limit: '))
    for i in range(1, message+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)




print(prime_number())