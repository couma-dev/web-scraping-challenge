#!/usr/bin/env python
# coding: utf-8

# NASA MARS NEWS
# 




from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pymongo
from splinter import Browser




executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)





url = 'https://redplanetscience.com/'
browser.visit(url)





html = browser.html
soup = BeautifulSoup(html, 'html.parser')
title = soup.find_all('div', class_ = 'content_title')[0].text
paragraph = soup.find_all('div', class_='article_teaser_body')[0].text
print(f'The latest news Title is: {title}')
print(f'The latest news Paragraph is: {paragraph}')





base_image_url = 'https://spaceimages-mars.com'

browser.visit(base_image_url)





button_click = browser.find_by_tag ('button')[1]
button_click.click()





html = browser.html
soup = BeautifulSoup(html, 'html.parser')
full_image_url = soup.find_all('img')
full_image_url





featured_url = soup.find('img', class_='fancybox-image')['src']
featured_url = base_image_url + featured_url
featured_url


# MARS FACTS



#use Pandas to scrape
import pandas as pd
url = 'https://galaxyfacts-mars.com'
tables = pd.read_html(url)
tables[0]




type(tables)





df = tables[0]
df.head()




html_table = df.to_html()
html_table



html_table.replace('\n', '')





#saving the table to html table
df.to_html('Mars Fact Table.html')


# MARS HEMISPHERE
# 
# 

# In[33]:


url = 'https://marshemispheres.com/'
browser.visit(url)





html = browser.html
soup = BeautifulSoup(html, 'html.parser')
results = soup.find_all('div', class_='item')
print(results[0])





hemisphere_image_urls = []
for result in results:
    title = result.find('h3').text
    img_url = result.find('img', class_='thumb')['src']
    hemisphere_image_urls.append({"title":title, "img_url": img_url })
    
hemisphere_image_urls




browser.quit()







