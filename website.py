"""["www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in"]

Write a python program to print website suffixes (com , org , net ,in) from this list
"""
websites = ["www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in"]
a = []
for i in websites:
    s = i.split('.')
    a.append(s[-1])
print(a)