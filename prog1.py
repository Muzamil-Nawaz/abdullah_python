import re

f = open("english.sorted.txt", "r")
words = f.read().split()
count=0
for word in words:
    b = re.search('^[aA]|[aA]$',word)
    if b!=None:
        print(word)
        count+=1


print(count)