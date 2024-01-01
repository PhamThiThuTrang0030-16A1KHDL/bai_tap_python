import requests
import xml.etree.ElementTree as ET
import csv

url = 'http://www.hindustantimes.com/rss/topnews/rssfeed.xml'

reponse = requests.get(url)
with open('rssfeed.xml', 'wb') as file:
    file.write(reponse.content)

tree = ET.parse('rssfeed.xml')
root = tree.getroot()

news_items = []
for item in root.findall('./chanel/item'):
    news = {}
    news['title'] = item.find('title').text
    news['link'] = item.find('link').text
    news['description'] = item.find('description').text
    news_items.append(news)
