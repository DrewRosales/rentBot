import requests
from bs4 import BeautifulSoup
def signIn():
    URL = 'https://houghtonoffcampushousing.appfolio.com/connect/users/sign_in'
    page = requests.get(URL)

    headers =  {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
    }

