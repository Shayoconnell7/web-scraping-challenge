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


def scrape():
    executable_path = {"executable_path": "chromedriver"}
    browser = Browser("chrome", **executable_path, headless=False)

    # +
    # browser = init_browser()

    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    html = browser.html
    soup = bs(html, "html.parser")

    # -

    # ## NASA Mars News

    sidebar = soup.find('ul', class_='item_list')
    print(sidebar)

    articles = sidebar.find_all('li')

    for article in articles [0]:
        teaser = article.select_one('div.article_teaser_body')
        title = article.select_one('div.content_title a')
        

    teaser.text

    title.text

    print(f"The latest headline: {title.text}.\nThe summary: {teaser.text}")

    # +
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    short_url = "https://www.jpl.nasa.gov"

    html = browser.html
    soup = bs(html, "html.parser")
    # -

    med_extension = soup.find("div", class_="carousel_items").a["data-fancybox-href"]
    med_image_url = (short_url+med_extension)
    print(f"url is {med_image_url}")

    extension = soup.find("li", class_="slide").a["data-fancybox-href"]
    featured_image_url = (short_url+extension)
    print(f"url is {featured_image_url}")

    # ## Mars Facts

    # +
    url = "https://space-facts.com/mars/"
    browser.visit(url)

    html = browser.html
    soup = bs(html, "html.parser")
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

    hemisphere_image_urls


    data = {
            "news_title": title,
            "news_paragraph": teaser,
            "featured_image": featured_image_url,
            "facts": mars_html_table,
            "hemispheres": hemisphere_image_urls,
           
        }
    return data
   # dictionary = dict(zip(teaser.text, title.text, featured_image_url, mars_html_table, hemisphere_image_urls))

 #"last_modified": last_modified






