import re

f = open("news.ycombinator.com.rss.xml", "r")
words = f.read()


# Task 1
updated_content = re.sub("<item>","<item>\n",words)
# Task 2
updated_content = re.sub("</item>","\n</item>\n",updated_content)
print(updated_content)


