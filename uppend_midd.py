""" 2. (3)Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1"""

s1 = 'nithis'
s2 = 'nithu'
b = []
h = []
l = []
for i in s1:
    b.append(i)
for m in s2:
    l.append(m)
c = len(b) / 2
if c % 2 == 0:
    e = c
else:
    e = c-0.5
f = int(e)
j = f + 1
h[:] = b[:j]
h.extend(l)
h.extend(b[-j:])
g = ''.join(h)
print(g)
