import requests, re
from bs4 import BeautifulSoup

headers = {
    "content-type"                  :   "application/x-www-form-urlencoded",
    "origin"                        :   "https://houghtonoffcampushousing.appfolio.com",
    "referer"                       :   "https://houghtonoffcampushousing.appfolio.com/connect/users/sign_in",
    "upgrade-insecure-requests"     :   "1",
    "user-agent"                    :   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"



}
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
    "user[password]"        :   "speedkills99",
    "commit"                :   "Log in"

}

result = s.post(
        URL,
        headers =   headers,
        data    =   payload,
        cookies =   s.cookies
        
)

print(result.url)


result1 = s.get(result.url)
str1 = result1.text
print(str1)