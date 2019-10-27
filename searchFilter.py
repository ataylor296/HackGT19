from googlesearch import search
import urllib
from bs4 import BeautifulSoup

searching = input("input: ")  
print(searching)  

for url in search('searching', stop=20):
    print(url)