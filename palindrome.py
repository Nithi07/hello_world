def is_palindrome(a):
    key = [a]
    if a == a[-1::-1]:
        return (f'{a} is an palindrome')
    else:
        return (f'{a} is an not palindrome')


message = input('>')
print(is_palindrome(message))