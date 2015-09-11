# web-kiosk
Web kiosk to display trending information from different subjects

 - USA news
 - weather 
 - sports 
 - movies
 - tech news
 - MTA info
 - more to come
 
# Dependencies
 - Flask
 - Requests
 - BeautifulSoup
 - lxml

#Installation
To start the kiosk all you will need to create a directory where to have all the kiosk files, then follow this steps:

- run  'pip install virtualenv' (if not already installed).
- run 'virtualenv flask' inside the the created folder.

Then run the following commands to install depedencies (assumming that you are in the kiosk dir):

- ./flask/bin/pip install requests
- ./flask/bin/pip install lxml
- ./flask/bin/pip install BeautifulSoup
- ./flask/bin/pip install flask
- ./flask/bin/pip install flask-mail

# Start Kiosk

After the installation just simply run:

- ./run.py (starts the Flask defaults web server on the localhost, port 5000)

You can also run:

 - ./ngrok http 5000 (which allows you to access outside the localhost )
