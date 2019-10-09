"""all the list methods explained"""

list1 = ['one', 'two', 'three']

a = list1.count('three')
print('count:       ', a)

# syntax important
list1.remove('one')
print('remove:      ', list1)


list1.sort()
print('sort:        ', list1)


list1.reverse()
print('reverse:     ', list1)

list1.clear()
print('clear:       ', list1)

list2 = ['one', 'two', 'three']
list3 = ['four', 'five', 'six']
list2.extend(list3)
print('extend:      ', list2)


list2.append(list3)
print('append:      ', list2)


list4 = ['seven', 'eight', 'nine', 'seven', 'ten']
x = list4.index('seven', 1, 4)
print('index:       ', x)
print('index;       ', list4.index('nine'))

list4.insert(5, 'eleven')
print('insert:      ', list4)
tup = (5, 6)
list4.insert(6, tup)
print('insert:      ', list4)


list4.pop()
print('pop:         ', list4)
list4.pop()
print('pop:         ', list4)
list4.pop()
print('pop:         ', list4)
list4.pop()
print('pop:         ', list4)#
# poped element
poped = list4.pop()
print('popped:      ', poped)

