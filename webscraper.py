import requests

from bs4 import BeautifulSoup

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import datetime

now = datetime.datetime.now()

#Email Content


#Extracting Hacker News Stories
def extract_news(url):
    print("Extracting Hacker News Stories...")
    cnt = ''
    cnt += ("<b>HN Top Stories: </b>\n" + "<br>" + "-" *50+ "<br>")
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
