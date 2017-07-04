import requests
from bs4 import BeautifulSoup
import summarize


url = "http://www.theverge.com/2013/8/1/4580718/fbi-can-remotely-activate-android-and-laptop-microphones-reports-wsj"
r  = requests.get(url)
data = r.text


print summarize.summarize_text(data)
