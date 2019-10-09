"""all dictnory functions explained"""


dic = {0: 'nithi',
       1: 'vijay',
       2: 'paul',
       3: 'ajith'}


dic.clear()
print('clear:       ', dic)
# -----------------------------------------
dic2 = {'4': 'satha',
       5: 'sivam',
       6: 'krish',
       7: 'kamal'
}
# ------------------------------------------
x = dic2.get('4')
print('get:         ', x)
print('get:         ', dic2)


# ------------------------------------------

# fromkey:

# vowels keys
keys = {'a', 'e', 'i', 'o', 'u' }
value = [1]

vowels = {key: value for key in keys}
# you can also use { key : value[:] for key in keys }
print(vowels)

# updating the value
value.append(2)
print(vowels)

# ------------------
key = {'a', 'b', 'c', 'd'}
value = ['*']                # it can be list, string, tuples anytype can accept
fr_key = dict.fromkeys(key, value)
print('fromkey:         ', fr_key)

# -----------------------------------------------------------


ite = dic2.items()
print('items:           ', ite)

# ----------------------------------------------------------------

val = dic2.values()
print('values:          ', val)

# --------------------------------------------------------

ke = dic2.keys()
print('keys:            ', ke)

# -------------------------------------------------------------

po = dic2.pop(7)
print('pop:             ', po)
print('pop:             ', dic2)

# ---------------------------------------------------------------


dic3 = {8: 'ninja',
        9: 'maanja',
        10: 'kanja'}


# setdefault


person = {'name': 'Phill', 'age': 22,}

age = person.setdefault('age')
print('person = ',person)
print('Age = ',age)
print(person)

# ---------------------------------------------------

ke = {'native': 'coimbatore'}
up = person.update(ke)
print('update:          ', up)


