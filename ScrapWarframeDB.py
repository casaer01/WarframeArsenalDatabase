import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://warframe.fandom.com/wiki/Weapon_Comparison#Primary')

soup = BeautifulSoup(response.text, 'html.parser')

# gun = soup.find_all('tr')[1].get_text()

for gun in soup.select('tr'):
    print(gun.get_text())

print(gun)