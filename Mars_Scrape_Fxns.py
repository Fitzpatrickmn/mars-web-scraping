from bs4 import BeautifulSoup as bs
import requests
import os 
import pandas as pd 
from splinter import Browser

def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)

mars_collection = {}

def newsfxn():
    browser = init_browser()

    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"

#Retrieve page with requests module
    response = requests.get(url)

# Create BeautifulSoup object; parse with 'html.parser'
    soup = bs(response.text, 'html.parser')

#Latest news title
    news_title = soup.find('div', class_='content_title').text
    #Accompanying news blurb for latest title
    news_blurb = soup.find('div', class_='rollover_description_inner').text

#     mars_collection['news_title'] = news_title
#     mars_collection['news_blurb'] = news_blurb
    browser.quit()
    
    return news_title, news_blurb


def imgfxn():
    browser = init_browser()
    nasaurl = 'https://www.jpl.nasa.gov'
    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url2)

    html = browser.html

    soup2 = bs(html, 'html.parser')

    step1 = soup2.find('img', class_='thumb')
    step2 = step1['src']
    featured_image_url = f"{nasaurl}"+f"{step2}"
    featured_image_url

#     mars_collection['featured_image_url'] = featured_image_url
    browser.quit()
    return featured_image_url

def weatherfxn():
    browser = init_browser()
    weatherURL = 'https://twitter.com/MarsWxReport'
    response = requests.get(weatherURL)
    weathersoup = bs(response.text, "html.parser")
    info = weathersoup.find("p", class_="TweetTextSize").text
#     for tweet in info:
#         mars_weather = tweet.find("p").text
#         if 'Sol' and 'pressure' in mars_weather:
#             break
#         else: 
#             pass
#     mars_collection['mars_weather'] = mars_weather
    browser.quit()
    return info 

def factsfxn():
    browser = init_browser()

    factsURL = 'https://space-facts.com/mars/'
    browser.visit(factsURL)

    tables = pd.read_html(factsURL)
    df = tables[0]
    df.columns = ["Parameter", "Values"]
    html_table = df.to_html(table_id="html_tbl_css",justify='left',index=False)

#     mars_collection['tables'] = html_table
    
    browser.quit()
    return html_table

def hemisfxn():
        browser = init_browser()

        hemiURL = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(hemiURL)

        hemihtml = browser.html

        hemisoup = bs(hemihtml, 'html.parser')
        
        s1 = hemisoup.find('img', class_='thumb')
        s2 = s1.findNext('img', class_='thumb')
        s3 = s2.findNext('img', class_='thumb')
        s4 = s3.findNext('img', class_='thumb')
        h = hemisoup.find('div', class_="description")
        t = h.a.text
        title = t.replace(' Enhanced', '')
        title

        h2 = h.findNext('div', class_="description")
        t2 = h2.a.text
        title2 = t2.replace(' Enhanced', '')
        title2

        h3 = h2.findNext('div', class_="description")
        t3 = h3.a.text
        title3 = t3.replace(' Enhanced', '')
        title3

        h4 = h3.findNext('div', class_="description")
        t4 = h4.a.text
        title4 = t4.replace(' Enhanced', '')
        title4
        
        hemisphere_titles = [title, title2, title3, title4]

        s1png = s1['src']
        s2png = s2['src']
        s3png = s3['src']
        s4png = s4['src']

        hemi_url1 = f"{hemiURL}"+f"{s1png}"
        hemi_url2 = f"{hemiURL}"+f"{s2png}"
        hemi_url3 = f"{hemiURL}"+f"{s3png}"
        hemi_url4 = f"{hemiURL}"+f"{s4png}"

        url_title = {'title': title, 'url': hemi_url1}
        url_title2 = {'title': title2, 'url': hemi_url2}
        url_title3 = {'title': title3, 'url': hemi_url3}
        url_title4 = {'title': title4, 'url': hemi_url4}

        hemisphere_urls_wtitle = [url_title, url_title2, url_title3, url_title4]

#         mars_collection['mars_hemis'] = hemisphere_urls_wtitle
        browser.quit()
        return hemisphere_urls_wtitle 




