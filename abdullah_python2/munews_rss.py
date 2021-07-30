import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime
import PyRSS2Gen




all_titles = []
all_links = []
all_dates = []
# Making a get request to 1st news page to get it's contnet using request library

x = requests.get('https://www.monmouth.edu/news/archives')


# Parsing contents of the above page into html nested text
soup = BeautifulSoup(x.text, 'html.parser')

# Finding main content section where all the articles are placed in the page
main_content = soup.find("div",attrs={'class':'content-wrapper clearfix fullwidth'})

# Finding all the article tags from the above main content to individually access the article
articles = main_content.find_all('article')

# Finding all the blocks with 'article-meta' class, because that's used for representing article publishing date
article_dates = soup.find_all('div',attrs={'class':'article-meta'})

# Counter to be used for iterating over article_dates
count=0
# Iterating over each article to get specific data
for article in articles:
    # Parsing current article in html form
    soup = BeautifulSoup(article.text, 'html.parser')
    # Finding anchor tag and printing it's href attribute regarding current article
    # print(article.find('a').attrs['href'])
    all_links.append(article.find('a').attrs['href'])
    # Finding anchor tag and printing it's title attribute regarding current article

    # print(article.find('a').attrs['title'])
    all_titles.append(article.find('a').attrs['title'].replace("“","\"").replace("”","\"").replace("’","'").replace("‘","'"))
    # printing articles dated with respect to article index number
    # print(article_dates[count].string)

    date_time_obj = datetime.strptime(article_dates[count].string.strip()+" 08:00:00", '%A, %B %d, %Y %H:%M:%S')
    date_time_obj = date_time_obj.replace(year=2020)
    all_dates.append(str(date_time_obj.strftime('%a, %d %b %Y %H:%M:%S')+" EST"))

    


    count+=1

# print(all_titles)




# Making a get request to 1st news page to get it's contnet using request library

x = requests.get('https://www.monmouth.edu/news/archives/page/2/')


# Parsing contents of the above page into html nested text
soup = BeautifulSoup(x.text, 'html.parser')

# Finding main content section where all the articles are placed in the page
main_content = soup.find("div",attrs={'class':'content-wrapper clearfix fullwidth'})

# Finding all the article tags from the above main content to individually access the article
articles = main_content.find_all('article')

# Finding all the blocks with 'article-meta' class, because that's used for representing article publishing date
article_dates = soup.find_all('div',attrs={'class':'article-meta'})

# Counter to be used for iterating over article_dates
count=0
# Iterating over each article to get specific data
for article in articles:
    # Parsing current article in html form
    soup = BeautifulSoup(article.text, 'html.parser')
    # Finding anchor tag and printing it's href attribute regarding current article
    all_links.append(article.find('a').attrs['href'])
    # Finding anchor tag and printing it's title attribute regarding current article

    # print(article.find('a').attrs['title'])    
    all_titles.append(article.find('a').attrs['title'].replace("“","\"").replace("”","\"").replace("’","'").replace("‘","'"))

    # parsing  article dates into rss acceptable format with respect to article index number
    date_time_obj = datetime.strptime(article_dates[count].string.strip()+" 08:00:00", '%A, %B %d, %Y %H:%M:%S')
    date_time_obj = date_time_obj.replace(year=2020)
    all_dates.append(str(date_time_obj.strftime('%a, %d %b %Y %H:%M:%S')+" EST"))
    count+=1
    


# Generating RSS items with data of articles
article_items = []
for i in range(len(all_titles)):
    article_items.append(PyRSS2Gen.RSSItem(
        title=all_titles[i],
        link=all_links[i],
        description="",
        pubDate=all_dates[i]

    ))


# Setting up RSS feed headers
rss = PyRSS2Gen.RSS2(
title = "Abdualrahman Allan",
link = "http://www.dalkescientific.com/Python/PyRSS2Gen.html",
description = "The latest news about PyRSS2Gen, Python library for generating RSS2 feeds",
lastBuildDate = datetime.now(),
items=article_items)


# Writing data to the RSS feed

rss.write_xml(open("rss_feed.xml","w+",encoding="utf-8"))




    

        

