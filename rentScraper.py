import requests, re
from bs4 import BeautifulSoup

"""
user[email]: drrosales99@gmail.com
user[password]: speedkills99
"""
payload = {
    "user[email]"           : "drrosales99@gmail.com",
    "user[password]"        : "speedkills99"
}

#def scrap():
s = requests.session()
URL = 'https://houghtonoffcampushousing.appfolio.com/connect/users/sign_in'

result = s.get(URL)
#token = re.search(r'(?<=<meta name="csrf-token" content=)\w+', result.text)
str = result.text
token=re.search(r'(?<=<meta name="csrf-token" content=")\S+',str)
token = token.group(0)
#auth = re.findall(r'\"(\S+)\"',token)
token = token[:-1]
print(token)
#print("\n\n\n\n")
#print(str)

result = s.post(
        URL,
        data = payload
)

print(result.url)
