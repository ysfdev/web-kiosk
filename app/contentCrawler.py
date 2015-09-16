try:
    import requests
except ImportError:
    print("Unable to Import Requests")

try:
	   
    import BeautifulSoup
    #from bs4 import BeautifulSoup
except ImportError:

    print("Unable to import BeautifulSoup")

try:

    from lxml import html
    from lxml import etree
except ImportError:
    print("Unable to import lxml")



# lists hold feeds content

news_feeds = []
news_feeds_desc = []
sports_feeds = []
weather_feeds = []
weather_desc_feeds = []
tech_feeds = []
movies_titles = []
movies_links = []
cybersecurity_feeds = []
mta_news_feeds = []


class IndexFeedsContent:
    '''
        Crawls and returns all the content for the index page containers
    '''

    def __init__(self):
        self.get_news_feeds()
        self.get_movies_feeds()
        self.get_weather_feeds()


    def get_news_feeds(self):

        url = 'http://news.yahoo.com/rss/us'

        #get news data

        r = requests.get(url)

        #find elements

        if r.status_code == 200:

            soup = BeautifulSoup(r.text, "xml") # parse the downloaded page into xml
            news_data = soup.findAll('title')   # finds all titles tags in document
            feeds_desc = soup.findAll('description')  # finds the description for each title tag


        news_feeds.clear()  # clear list before appending to it
        news_feeds_desc.clear()

        i = 1  # counter

        #get data first only 10 headings
        for news in news_data[2:11]:

             news_feeds.append(news.text)
             news_feeds_desc.append(feeds_desc[i].text)
             i =+ 1

    def get_movies_feeds(self):

        url = 'http://www.fandango.com/rss/top10boxoffice.rss'

        #get news data

        r = requests.get(url)

        #find elements

        if r.status_code == 200:

            soup = BeautifulSoup(r.text, "xml")
            titles = soup.findAll('title')
            image_links = soup.findAll('enclosure') # contains images links


        movies_titles.clear()  # clear list before appending to it
        movies_links.clear()

        title_counter = 2
        image_counter = 0

        #get data first 10  headings
        for feeds in titles[2:12]:

            movies_links.append(str(image_links[image_counter])[45:-3]) # appends only href links
            movies_titles.append(str(titles[title_counter].text)[2:]) # append text after second index

            title_counter += 1
            image_counter += 1




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


class Page2FeedsContent:
    '''
        Crawls and returns all the content for page containers
    '''

    def __init__(self):
        self.get_tech_feeds()
        self.get_cybersecurity_feeds()
        self.get_sports_feeds()
        self.get_mta_feeds()

    def get_sports_feeds(self):

        url = 'http://sports.espn.go.com/espn/rss/news'

        #get news data

        r = requests.get(url)

        #find elements

        if r.status_code == 200:

            soup = BeautifulSoup(r.text, "xml") # parse the downloaded page into xml
            sports_data = soup.findAll('title') # finds all the title tags


        sports_feeds.clear()  # clear list before appending to it

        #get data first 10 headings
        for feeds in sports_data[2:12]:

                sports_feeds.append(feeds.text) # appends the feeds to sports_feeds list

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
        for feeds in feeds_data[2:12]:

            cybersecurity_feeds.append(feeds.text)


    def get_mta_feeds(self):

        url = 'http://www.mta.info/mta-news'
        page = requests.get(url)

        tree = html.fromstring(page.text)
        titles = tree.xpath(".//*[@id='block-views-mta-news-stories-block']/div/div/div/div/div/div/a")

        mta_news_feeds.clear() #  clear list before appending

        for title in titles[2:7]: # get first 10 titles

            mta_news_feeds.append(title.text)
