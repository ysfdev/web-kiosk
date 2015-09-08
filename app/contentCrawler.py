from pyvirtualdisplay import Display
from selenium import webdriver
from time import sleep
import requests
from bs4 import BeautifulSoup


# lists hold feeds content


news_feeds = []
news_feeds_desc = []
sports_feeds = []
weather_feeds = []
weather_desc_feeds = []
tech_feeds = []
movie_feeds = []
cybersecurity_feeds = []



class getIndexFeedsContent:



    def __init__(self):
        print("on")
        #self.get_news_feeds()
        #self.get_sports_feeds()
        #self.get_weather_feeds()


    def get_news_feeds(self):

        url = 'http://rssfeeds.usatoday.com/usatoday-NewsTopStories'

        #get news data

        r = requests.get(url)

        #find elements

        if r.status_code == 200:

            soup = BeautifulSoup(r.text, "xml")
            news_data = soup.findAll('title')
            feeds_desc = soup.findAll('description')


        news_feeds.clear()  # clear list before appending to it
        news_feeds_desc.clear()

        i = 1  # counter
        #get data first 10 headings
        for news in news_data[2:11]:

             news_feeds.append(news.text)
             news_feeds_desc.append(feeds_desc[i].text)
             i =+ 1




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

        #iterate weather dataDOD
        for feeds in feeds_titles[1:]:

             weather_feeds.append(feeds.text)
             weather_desc_feeds.append(feeds_desc[i].text) # feed titles descriptions
             i += 1

class getPage2FeedsContent:


    def __init__(self):

        print("on")
        #self.get_tech_feeds()
        #self.get_cybersecurity_feeds()
        #self.get_dod_feeds()

    def get_movie_feeds(self):

        url = 'http://movieweb.com/rss/new-movies/'

        #get news data

        r = requests.get(url)

        #find elements

        if r.status_code == 200:

            soup = BeautifulSoup(r.text, "xml")
            feeds_data = soup.findAll('title')


        movie_feeds.clear()  # clear list before appending to it

        #get data first 10 headings
        for feeds in feeds_data[1:11]:

            movie_feeds.append(feeds.text)

    def get_tech_feeds(self):

        url = "http://www.cnet.com/rss/news/"

        #get news data

        r = requests.get(url)

        #find elements

        if r.status_code == 200:

            soup = BeautifulSoup(r.text, "xml")
            feeds_data = soup.findAll('title')


        tech_feeds.clear()  # clear list before appending to it

        #get data first 10 headings
        for feeds in feeds_data[2:12]:

             tech_feeds.append(feeds.text)

    def get_cybersecurity_feeds(self):

        url = 'http://feeds.feedburner.com/TheHackersNews'


        #get news data

        r = requests.get(url)

        #find elements

        if r.status_code == 200:

            soup = BeautifulSoup(r.text, "xml")
            feeds_data = soup.findAll('title')


        cybersecurity_feeds.clear()  # clear list before appending to it

        #get data first 10 headings
        for feeds in feeds_data[1:11]:

            cybersecurity_feeds.append(feeds.text)

