"""  8. (3)Given a string, return the sum and average of the digits that appear in the string,
ignoring all other characters
"""
message = input('Enter: ')
a = []
for i in message:
    if i.isdigit():
        a.append(int(i))
tot = sum(a)
ave = tot / len(a)
print(f'sum of digit: {tot}\n average of digits: {ave}')





