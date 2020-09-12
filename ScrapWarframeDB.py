import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://warframe.fandom.com/wiki/Weapon_Comparison#Primary')

soup = BeautifulSoup(response.text, 'html.parser')

# gun = soup.find_all('tr')[1].get_text()


primaryWeaponsData = soup.select('div[title="Primary"] tr td')

count = 0
for gun in primaryWeaponsData:
    print(gun.get_text() + "     =     " + str(count))
    count+= 1


# for x in range(0,12):

#     print(dataArsenal[x].get_text())



# print(dataArsenal.get_text())

