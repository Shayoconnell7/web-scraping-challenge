from flask import Flask, jsonify
import pandas as pd
import requests
from splinter import Browser
from bs4 import BeautifulSoup as bs
import datetime as dt
import time


## Get Latest News    
def mars_news_f(browser):

    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    

    html = browser.html
    soup = bs(html, "html.parser")


    time.sleep(7)
    sidebar = soup.find('ul', class_='item_list')
    print(sidebar)

    articles = sidebar.find_all('li')

    for article in articles [0]:
        teaser = article.select_one('div.article_teaser_body')
        title = article.select_one('div.content_title a')
        

    teaser_text = teaser.text

    title_text = title.text

    print(f"The latest headline: {title_text}.\nThe summary: {teaser_text}")

    return teaser_text, title_text
    
## Get Featured Image
def featured_image_f(browser):
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)

    browser.click_link_by_partial_text("FULL")
    browser.click_link_by_partial_text("more info")
    browser.click_link_by_partial_href('hires')
    featured_image_url = browser.url
    

    return featured_image_url
    
## Get Mars Facts
def mars_facts_f(browser):
    
    url = "https://space-facts.com/mars/"
    browser.visit(url)

    tables = pd.read_html(url)
    tables

    mars_info = pd.DataFrame(tables[0])
    
    mars_html_table = mars_info.to_html(header=False, index=False)

    mars_html_table.replace('\n', '')

    return mars_html_table

## Get Mars Hemispheres
def hemisphere_f(browser):
   
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)

    hemisphere_image_urls = []

    links = browser.find_by_css("a.product-item h3")

    for i in range(len(links)):
        hemisphere = {}
        
        browser.find_by_css("a.product-item h3")[i].click()
        
        hemisphere['title'] = browser.find_by_css("h2.title").text
        
        sample_elem = browser.links.find_by_text('Sample').first
        hemisphere['img_url'] = sample_elem['href']
        
        hemisphere_image_urls.append(hemisphere)
        
        browser.back()


    return hemisphere_image_urls

#scrape it all and add to one dictionary
def scrape():
    
    executable_path = {"executable_path": "chromedriver.exe"}
    browser = Browser("chrome", **executable_path, headless=False)

    data = {
            "news_title": mars_news_f(browser)[1],
            "news_paragraph": mars_news_f(browser)[0],
            "featured_image": featured_image_f(browser),
            "facts": mars_facts_f(browser),
            "hemispheres": hemisphere_f(browser),
            "last_modified": dt.datetime.now()
        }
    return data

if __name__ == "__main__":
   # If running as script, print scraped data
   print(scrape())
 






