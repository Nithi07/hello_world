def limit(speed):
    output = 0
    if speed < 70:
        return ('ok')
    else:
        z = speed / 5
        i = round(z)
        a = i-14
        output += a
        if output >= 12:
            return ('your liscense is cancelled')
        else:
            return (f'you demerit point is {output}')



put = int(input('max speed: '))
print(limit(put))