from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    
    '============================================================='
    '///// MARS - ARTICLES  /////'
    '============================================================='

    '======================================================'
    '//// INITATION CODE ////'
    soup = ''
    browser = init_browser()
    time.sleep(.3)
    url = 'https://mars.nasa.gov/news'
    browser.visit(url)
    time.sleep(1)
    html = browser.html
    soup = bs(html, "html.parser")
    '======================================================'
    '//// VARIABLES ////'
    all_scrape_data = {}
    news_title = []
    news_p = []
        
    '======================================================'
    '//// SCRAPE METHODS ////'
    
    '// find titles //'
    news_titles = soup.find_all('div', class_='content_title')
   
    for titles in news_titles :             # ITERATE TRHOUGH ARTICLE DUMP
        news_title.append(titles.text)        # ADD TEXT TO LIST  

    # all_scrape_data["news_title"]= news_title  # ADD LIST TO DICTIONARY    
    
    '// find articles //'
    news_p1 = soup.find_all('div', class_='article_teaser_body')
    
    for articles in news_p1 :               # ITERATE TRHOUGH ARTICLE DUMP
        news_p.append(articles.text)        # ADD TEXT TO LIST  
    # all_scrape_data["news_p"] = news_p  # ADD LIST TO DICTIONARY    

    #browser.quit()


    '============================================================='
    '///// MARS  FEATURED IMAGE /////'
    '============================================================='
    '// find image //'  
    time.sleep(.2)
    soup = ''
    urls = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(urls)
    time.sleep(1)
    html = browser.html
    soup = bs(html, "html.parser")

    img_uurl = soup.find('a', class_= 'button fancybox')
    lg_image_url = img_uurl.get('data-fancybox-href')
    featured_image_url = f'https://www.jpl.nasa.gov{lg_image_url}'
#   print(featured_image_url)
    #browser.quit()
    

    
    '============================================================='
    '///// MARS WEATHER /////'
    '============================================================='
    browser = init_browser()
    soup = ''
    time.sleep(.3)
    urls2 = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(urls2)
    time.sleep(1)
    html = browser.html
    soup = bs(html, "html.parser")

    grab_weather = soup.find('p', class_ ="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text" )
    # print("done scrapping!")
    mars_weather = grab_weather.text
    # print(f'mars weather report : {mars_weather} ')
    #browser.quit()



    '============================================================='
    '///// MARS FACTS  /////'
    '============================================================='
    browser = init_browser()
    soup = ''
    time.sleep(.3)
    urls3 = 'https://space-facts.com/mars/'
    browser.visit(urls3)
    time.sleep(1)
    html = browser.html
    soup = bs(html, "html.parser")

    mars_tb = []
    mars_cells =[]

    tables = soup.find( 'table', id="tablepress-p-mars")
    mars_cells = tables.find_all('td')   

    for elementz in mars_cells:
        mars_tb.append(elementz.text)

    # #browser.quit()

    # # LOOK AT THIS ACTIVITY ON HOW TO DO THIS IN HTML WIHT OUR mars_tb  list        
    # # InClassActivities\12-Web-Scraping-and-Document-Databases\3\Activities\03-Ins_Render_List\Solved

    # # <table style="width:100%">
    # # {% for item in list %}
    # # <tr>
    # # <th>{{ mars_tb[] }}</th>
    # # </tr>
    # # {% endfor %}


    '============================================================='
    '///// MARS HEMISPHERES /////'
    '============================================================='
    soup = ''
    browser = init_browser()
    time.sleep(.3)
    urls4 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(urls4)
    time.sleep(1)
    html = browser.html
    soup = bs(html, "html.parser")

    links1 = []
    links2lg = []
    hem_list = []
    img_list =[]

    soup_dump   = soup.find('div',  class_="collapsible results" )
    links1      = soup_dump.find_all('div', class_="item" )
    
    for elements1 in links1:
        links2lg.append(elements1.a['href'])

    descp =soup_dump.find_all('h3')
    
    for stuffs in descp:
        hem_list.append(stuffs.text) 

    soup = ''
    #browser.quit()


    for stuff in links2lg :  
  
        browser = init_browser()
        time.sleep(1)
        address = 'https://astrogeology.usgs.gov/' 
        #   elements2 = links2lg[1]
        urls6 = f'{address}{stuff}'    
        browser.visit(urls6)
        # print(urls6)
        time.sleep(1)
        html = browser.html
        soup = bs(html, "html.parser")
        large_linkz = soup.find_all('li')[0]
        img_list.append(large_linkz.a['href'])
        time.sleep(.5)
        # print(img_list)
        soup = ''
        large_linkz =''
        #browser.quit()

    # print("I am done scrapping MARS LG IMAGE LINKS")     

    hemisphere_image_urls = [
                            {"title": hem_list[0], "img_url": img_list[0]},
                            {"title": hem_list[1], "img_url": img_list[1]},
                            {"title": hem_list[2], "img_url": img_list[2]},
                            {"title": hem_list[3], "img_url": img_list[3]},
                            ]

    all_scrape_data["hemisphere_image_urls"] = hemisphere_image_urls # ADD LIST TO DICTIONARY       
 
    '============================================================='
    '///// CONSOLIDATE ALL DATA INTO FINAL DICT  /////'
    '============================================================='

        
    all_scrape_data = {
                    "news_p"                : news_p,  
                    "news_title"            : news_title, 
                    "featured_image_url"    : featured_image_url,
                    "mars_weather"          : mars_weather,
                    "mars_info_table"       : mars_tb,
                    "hemisphere_image_urls" : hemisphere_image_urls
                    }   

    browser.quit()


    return all_scrape_data


# x = scrape_info()
# print(x)
'============================================================='
'///// END OF ALL CODE  /////'
'============================================================='