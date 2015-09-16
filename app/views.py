from app import app
from flask import render_template, request, redirect
from app import contentCrawler
from time import sleep


@app.route('/')
@app.route('/kiosk')

def index():

    # start feeds content crawling

    contentCrawler.IndexFeedsContent()

    news_feeds = contentCrawler.news_feeds

    weather_feeds = contentCrawler.weather_feeds
    weather_feeds_description = contentCrawler.weather_desc_feeds
    news_feeds_description = contentCrawler.news_feeds_desc
    movies_titles = contentCrawler.movies_titles
    movies_links = contentCrawler.movies_links

    return render_template("index.html",
                news_content=news_feeds,
                news_desc_content=news_feeds_description,
                weather_content=weather_feeds,
                weather_desc_content=weather_feeds_description,
                movies_titles=movies_titles,
                movies_links=movies_links)





@app.route('/page2')

def page2():

    contentCrawler.Page2FeedsContent()

    tech_feeds = contentCrawler.tech_feeds
    cyber_feeds = contentCrawler.cybersecurity_feeds
    sports_feeds = contentCrawler.sports_feeds
    mta_feeds = contentCrawler.mta_news_feeds

    return render_template("page2.html",
                           tech_content=tech_feeds,
                           cyber_content=cyber_feeds,
                           sports_content=sports_feeds,
                           mta_content=mta_feeds)



@app.route ("/sms-feeds")

def send_sms_feeds():
    '''

    :return: replies top feeds for sms requests
    '''

    contentCrawler.IndexFeedsContent()

    news_feeds = contentCrawler.news_feeds
    sports_feeds = contentCrawler.sports_feeds
    weather_feeds = contentCrawler.weather_feeds

    message = ("---------------------------------" + "\n"
               " **KIOSK TOP HEADLINES** " + "\n"
               "---------------------------------" + "\n"
               "News: " + news_feeds[1] + "\n"
               "---------------------------------" + "\n"
               "Sports: " + sports_feeds[0] + "\n"
               "---------------------------------" + "\n"
               "Weather: " + weather_feeds[0])

    resp = twilio.twiml.Response()
    resp.message(message)

    return str(resp)

