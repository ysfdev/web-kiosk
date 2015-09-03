from app import app
from flask import render_template
from app import contentCrawler

#display = Display(visible=0, size=(720, 450))
#display.start()


@app.route('/')
@app.route('/kiosk')

def index():

    # start feeds content crawling
    contentCrawler.getFeedsContent()

    news_feeds = contentCrawler.news_feeds
    sports_feeds = contentCrawler.sports_feeds
    weather_feeds = contentCrawler.weather_feeds
    weather_description_feeds = contentCrawler.weather_desc_feeds


    return render_template("index.html",
                news_content=news_feeds,
                sports_content=sports_feeds,
                weather_content=weather_feeds,
                weather_desc_content=weather_description_feeds)


