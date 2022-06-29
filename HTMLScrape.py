import requests
from bs4 import BeautifulSoup

link = "http://google.com"


result = requests.get(link)
print(result.status_code)
print(result.headers)
src = result.content
print(src)
soup = BeautifulSoup(src, 'html.parser')

print(soup.prettify())
soup.title
soup.find_all('a')


