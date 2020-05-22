import requests
from bs4 import BeautifulSoup


"""
user[email]: drrosales99@gmail.com
user[password]: speedkills99
authenticity_token: o6X+GJr6j/vV8gIbenFdwjlGRoMDmqLLrtnyQ2v+fBWzqA2cEG2yVmTbyzmYKXDtzSK2ZiI3X4rsUDEDe0qWyg==

"""
payload = {
    "user[email]"           : "drrosales99@gmail.com",
    "user[password]"        : "speedkills99",
    "authenticity_token"    : "o6X+GJr6j/vV8gIbenFdwjlGRoMDmqLLrtnyQ2v+fBWzqA2cEG2yVmTbyzmYKXDtzSK2ZiI3X4rsUDEDe0qWyg=="
}

#def scrap():
s = requests.session()
URL = 'https://houghtonoffcampushousing.appfolio.com/connect/users/sign_in'

result = s.get(URL)
#tree = html.fromstring(result.text)
#token = list(set(tree.xpath("//input[@name='authenticity_token']/@value")))[0]

result = s.post(
        URL,
        data = payload
)

print(result.url)
