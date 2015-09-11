
#MODULES
from pyvirtualdisplay import Display

#display = Display(visible=0, size=(720, 450))
#display.start()

'''
class feedsContents:

    # holds feeds content

    news_feeds = []
    sports_feeds = []
    weather_feeds = []

    def __init__(self):

        self.browser = webdriver.Firefox()
        self.get_news_feeds()
        self.get_sports_feeds()
        self.get_weather_feeds()


    def __del__(self):

        self.browser.close()

        # clear lists contents
        self.news_feeds = []
        self.sports_feeds = []
        self.weather_feeds = []

    def get_contents(self):

        self.browser.close()
        #display.stop()


    def get_news_feeds(self):


        url = 'http://edition.cnn.com/specials/last-50-stories'

        #get news data

        self.browser.get(url)

        #find elements

        news_data = self.browser.find_elements_by_css_selector('.cd__headline-text')

        #display data first 10 headings
        for news in news_data[:10]:

             self.news_feeds.append(news.text)

        return self.news_feeds


    def get_sports_feeds(self):


        url = 'http://www.usnews.com/news/sports'

        #get news data

        self.browser.get(url)

        #find elements

        sports_data = self.browser.find_elements_by_css_selector('.h.h-bigger>a')

        #display data first 10 headings
        for feeds in sports_data[:10]:

             self.sports_feeds.append(feeds.text)

        return self.sports_feeds

    def get_weather_feeds(self):

        url = 'http://www.accuweather.com/en/weather-news'

        #get news data

        self.browser.get(url)

        #find elements

        weather_data = self.browser.find_elements_by_css_selector('.info>h4>a')

        #display data first 10 headings
        for feeds in weather_data[:10]:

             self.weather_feeds.append(feeds.text)

        return self.weather_feeds
'''

def print_hello():

    print("Hello Im a Module")

