import requests, re
from bs4 import BeautifulSoup



#Creates a session to store
s = requests.session()

#Login for tennant portal
URL = 'https://houghtonoffcampushousing.appfolio.com/connect/users/sign_in'

#get request at portal
result = s.get(URL)

#convert portal to String
str = result.text

#Regular expressions to find the token beginning with the HTML tag
token=re.search(r'(?<=<meta name="csrf-token" content=")\S+',str)
token = token.group(0)

#Subtracts the last character \" from the String
token = token[:-1]
print(token)


payload = {
    "utf8"                  :   "%25E2%259C%2593",
    "authenticity_token"    :   token,
    "user[email]"           :   "drrosales99@gmail.com",
    "user[password]"        :   "speedkills99"
    "commit"                :   "Log in"

}

result = s.post(
        URL,
        data = payload
)

print(result.url)
