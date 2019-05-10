from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.clien.net"
urlPark = "/service/board/park"
html = urlopen(url + urlPark)
source = html.read()
html.close()

soup = BeautifulSoup(source, "html.parser")

for tag in soup.select('a.list_subject[data-role=cut-string]'):
    print(tag.span.get_text() + ' : ' + url + tag['href'])




