from pyvirtualdisplay import Display
from selenium import webdriver
from time import sleep
import requests
from bs4 import BeautifulSoup


# lists hold feeds content


news_feeds = []
sports_feeds = []
weather_feeds = []
weather_desc_feeds = []



class getFeedsContent:



    def __init__(self):

        self.get_news_feeds()
        self.get_sports_feeds()
        self.get_weather_feeds()


    def __del__(self):

        self.browser.close()

    def get_news_feeds(self):

        url = 'http://www.usnews.com/rss/news'

        #get news data

        r = requests.get(url)

        #find elements

        if r.status_code == 200:

            soup = BeautifulSoup(r.text, "xml")
            news_data = soup.findAll('title')


        news_feeds.clear()  # clear list before appending to it

        #get data first 10 headings
        for news in news_data[1:11]:

             news_feeds.append(news.text)




    def get_sports_feeds(self):


        url = 'http://www.usnews.com/rss/news'

        #get news data

        r = requests.get(url)

        #find elements

        if r.status_code == 200:

            soup = BeautifulSoup(r.text, "xml")
            sports_data = soup.findAll('title')

        sports_feeds.clear()  # clear list before appending to it

        #get data first 10 headings
        for feeds in sports_data[1:11]:

             sports_feeds.append(feeds.text)

    def get_weather_feeds(self):

        url = 'http://www.rssweather.com/zipcode/10001/rss.php'

        #get news data

        r = requests.get(url)

        #find elements

        if r.status_code == 200:

            soup = BeautifulSoup(r.text, "lxml")
            feeds_titles = soup.findAll('title')
            feeds_desc = soup.findAll('description')

        weather_feeds.clear()  # clear list before appending to it
        weather_desc_feeds.clear()

        i = 1  # counter for weather feeds

        #iterate weather data
        for feeds in feeds_titles[1:]:

             weather_feeds.append(feeds.text)
             weather_desc_feeds.append(feeds_desc[i].text) # feed titles descriptions
             i += 1

