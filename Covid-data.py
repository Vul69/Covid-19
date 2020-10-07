from bs4 import BeautifulSoup
import requests
url = "https://www.worldometers.info/coronavirus/"
res = requests.get(url)

soup = BeautifulSoup(res.content, 'lxml')

numbers = soup.find_all('div', {"class": "maincounter-number"})

total_cases = numbers[0].span.text
deaths = numbers[1].span.text
recovered = numbers[2].span.text
print("World Status")
print("Total cases: ", total_cases)
print("Deaths: ", deaths)
print("Recovered: ", recovered)
