from urllib.request import urlopen
from bs4 import BeautifulSoup

site = "https://www.cebupacificair.com"
page = urlopen(site)

soup = BeautifulSoup(page, 'html.parser')


a = soup.find('div',class_='flyout-container')

print(a)



for link in soup.find_all('li',class_="flyout-selector"):
    print(link.get_text())



# print(name_box)