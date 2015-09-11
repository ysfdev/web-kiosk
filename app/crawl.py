import requests
from bs4 import BeautifulSoup
from lxml import html
from lxml import etree

page = requests.get('http://www.mta.info/mta-news')
print("Got URL")

tree = html.fromstring(page.text)
titles = tree.xpath(".//*[@id='block-views-mta-news-stories-block']/div/div/div/div/div/div/a")



for title in titles[1:]:

    print(title.text)


# MTA NEWS

'''
if r.status_code == 200:

    soup = BeautifulSoup(r.text, "lxml")
    title = soup.findAll('title')
    image_links = soup.findAll('description') # contains images links
    #feeds_desc = soup.findAll('description')

    movies = []
    links = []

    print(image_links)

    title_counter = 2
    counter = 0
    i = 0

    for feeds in title[2:]:

        name = feeds.contents[0]
        link = feeds.get('p')

        print(name)


        title_counter += 1
        counter += 1



    for link in range(9):

        #print(movies[i])
        print(links[i])
        i += 1
    '''





