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

# ## JPL Mars Space Images - Featured Image
#

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

# +
url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url)

html = browser.html
soup = bs(html, "html.parser")

# +
# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

# +

sidebar = soup.find(class_='collapsible_results')

categories = sidebar.find_all('item')

category_list = []
url_list = []
book_url_list = []

for category in categories:
    title = category.text.strip()
    category_list.append(title)
    book_url = category.find('a')['href']
    url_list.append(book_url)

book_url_list = ['http://books.toscrape.com/' + url for url in url_list]

titles_and_urls = zip(category_list, book_url_list)

try:
    for title_url in titles_and_urls:
        browser.click_link_by_partial_text('next')
except ElementDoesNotExist:
    print("Scraping Complete")
# -

browser.click_link_by_partial_text('Enhanced')

links_found = browser.links.find_by_partial_text('Enhanced')

links_found.text


images_a = browser.find_by_css("a.product-item h3")

img_dict = {"title" : "", "img_url" : ""}

hemisphere_image_urls = []

for image in images_a:
    browser.links.find_by_partial_text('Enhanced').click
    img_dict.update(img_url = image)
    img_dict["title"] = image.text
    hemisphere_image_urls.append(img_dict)
    print(image)

img_dict

hemisphere_image_urls

print(images_a)

images_a.text

urls.text

browser.find_by_css('item').first.value









hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    {"title": "Cerberus Hemisphere", "img_url": "..."},
    {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    {"title": "Syrtis Major Hemisphere", "img_url": "..."},
]


