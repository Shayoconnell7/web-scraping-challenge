# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.7.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

from flask import Flask, jsonify
import pandas as pd
import requests
from splinter import Browser
from bs4 import BeautifulSoup as bs
import datetime as dt
import time
from selenium import webdriver


    
def mars_news_f(browser):

    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

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
    # +

def featured_image_f(browser):
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)

    html = browser.html

    # -
    browser.click_link_by_partial_text("FULL")
    browser.click_link_by_partial_text("more info")
    browser.click_link_by_partial_href('hires')
    featured_image_url = browser.url
    

    return featured_image_url
    # ## Mars Facts
def mars_facts_f(browser):
    # +
    url = "https://space-facts.com/mars/"
    browser.visit(url)

    html = browser.html
    
    # -

    tables = pd.read_html(url)
    tables

    mars_info = pd.DataFrame(tables[0])
    mars_info.columns = ['Mars', 'Data']
    mars_info.set_index('Mars', inplace=True)

    mars_info

    mars_html_table = mars_info.to_html()
    mars_html_table

    mars_html_table.replace('\n', '')

    return mars_html_table

def hemisphere_f(browser):
    # ## Mars Hemispheres

    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)

    # +
    hemisphere_image_urls = []

    # First, get a list of all of the hemispheres
    links = browser.find_by_css("a.product-item h3")

    # Next, loop through those links, click the link, find the sample anchor, return the href
    for i in range(len(links)):
        hemisphere = {}
        
        # We have to find the elements on each loop to avoid a stale element exception
        browser.find_by_css("a.product-item h3")[i].click()
        
        # Get Hemisphere title
        hemisphere['title'] = browser.find_by_css("h2.title").text
        
        # Next, we find the Sample image anchor tag and extract the href
        sample_elem = browser.links.find_by_text('Sample').first
        hemisphere['img_url'] = sample_elem['href']
        
        # Append hemisphere object to list
        hemisphere_image_urls.append(hemisphere)
        
        # Finally, we navigate backwards
        browser.back()
    # -

    return hemisphere_image_urls

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
 






