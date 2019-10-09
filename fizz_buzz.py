def fizz_buzz(number):
    """Write a function called fizz_buzz that takes a number.

    If the number is divisible by 3, it should return “Fizz”.
    If it is divisible by 5, it should return “Buzz”.
    If it is divisible by both 3 and 5, it should return “FizzBuzz”.
    Otherwise, it should return the same number.
    """
    if not number % 5 == 0 and number % 3 == 0:
        return ('Fizz')
    elif not number % 3 == 0 and number % 5 == 0:
        return ('Buzz')
    elif number % 3 == 0 and number % 5 == 0:
        return ('fizzbuzz')
    else:
        return (number)


num = int(input('enter the  number: '))
print(fizz_buzz(num))