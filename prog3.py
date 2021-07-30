import re

f = open("news.ycombinator.com.rss.xml", "r")
words = f.read()

titles = re.findall("<title>(.*?)</title>",words)[1:]
print(titles)


links = re.findall("<link>(.*?)</link>",words)[1:]
print(links)

print(words)