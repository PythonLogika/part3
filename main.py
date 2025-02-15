import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

data = []

for i in range(len(quotes)):
    line = quotes[i].text + " - " + authors[i].text + "\n"
    data.append(line) 

with open("quotes.txt", "w", encoding="utf-8") as file:
    for line in data:
        file.write(line)

# ДЗ: https://cutt.ly/LbT7IZY
# https://scrapingclub.com/exercise/list_basic/?page=1
