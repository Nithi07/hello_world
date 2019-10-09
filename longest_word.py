""" 7. (2)Write a python program to find the longest word in a given sentence"""
def longest_word():
    message = input('write here:  ')
    key = message.split(' ')
    dic = {}
    for i in key:
        dic[len(i)] = i
    return dic.setdefault(max(dic.keys()))


print(longest_word())




