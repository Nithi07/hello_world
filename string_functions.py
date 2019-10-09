"""all the string methods explained"""

st = 'No means no'
a = st.isalpha()
print('isalpha:        ', a)

b = st.encode()
print('encode:         ', b)

c = st.split(' ')
print('split:          ', c)

d = st.isspace()
print('isspace:        ', d)

e = st.isdigit()
print('isdigit:        ', e)

f = st.islower()
print('islower:        ', f)


g = "".join(c)
print('join:           ', g)

h = st.center(50, '*')
print('center:         ', h)
print('ljust:          ', st.ljust(50, '*'))
print('rjust           ', st.rjust(50, '*'))

i = st.lstrip('No')
print('lstrip:         ', i)

j = st.rstrip('no')
print('rstrip:         ', j)

k = st.strip('no')
print('strip:          ', k)

l = st.rsplit()
print('rsplit1:        ', l)

m = st.rsplit(' ', 1)
print('rsplit2:        ', m)

n = st.rsplit('n', 2)
print('rsplit3:        ', n)

o = st.count('no')
print('count:          ', o)

p = st.endswith('means no')
print('endswith:       ', p)
print('startswith:     ', st.startswith('No'))

# casefold also similar to lower()
q = st.casefold()
print('casefold:       ', q)
print('capitalize:     ', st.capitalize())
# capitalize used to initial became caps

r = st.splitlines()
print('splitlines:     ', r)
# it split the line, each line has one index

s = st.expandtabs(5)
print('expandtabs:     ', s)
# it is using only when "\t" to be used.

st2 = 'beautiful {} nature'
t = st2.format('of')
print('format:         ', t)

u = st.isprintable()
print('isprintable:    ', u)

v = st.isidentifier()
print('isidentifier:   ', v)
# when strings(v) comes non space that is identifier otherwise it come with space it is false.

w = st.partition('means')
print('partition:      ', w)
# it split what we give into partition() separately and other strings splited separately

x = st.swapcase()
print('swapcase:       ', x)

y = st.title()
print('title:          ', y)

z_fill = '+&^%wjkk'
z = z_fill.zfill(40)
print('zfill;          ', z)

#map()
N=int(input())
V=list(map(int,input().split()))
print(V.count(max(V)))




