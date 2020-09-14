import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://warframe.fandom.com/wiki/Weapon_Comparison#Primary')

soup = BeautifulSoup(response.text, 'html.parser')

# gun = soup.find_all('tr')[1].get_text()

# Values to insert: Secondary,Melee, Robotic, Atmos Arch-Gun, Arch-Gun, Arch-Melee
primaryWeaponsData = soup.select('div[title="Primary"] tr td')

# count = 0
# for gun in primaryWeaponsData:
#     print(gun.get_text() + "     =     " + str(count))
#     count+= 1

pWeapon =[]

for weapon in range(0,len(primaryWeaponsData), 12):
    print("Number is " + str(weapon))
    print(primaryWeaponsData[weapon].get_text())
    print(primaryWeaponsData[weapon+1].get_text())
    print(primaryWeaponsData[weapon+2].get_text())
    print(primaryWeaponsData[weapon+3].get_text())
    print(primaryWeaponsData[weapon+4].get_text())
    print(primaryWeaponsData[weapon+5].get_text())
    print(primaryWeaponsData[weapon+6].get_text())
    print(primaryWeaponsData[weapon+7].get_text())
    print(primaryWeaponsData[weapon+8].get_text())
    print(primaryWeaponsData[weapon+9].get_text())
    print(primaryWeaponsData[weapon+10].get_text())
    print(primaryWeaponsData[weapon+11].get_text())
    print(primaryWeaponsData[weapon+12].get_text())
    # print(primaryWeaponsData[weapon+13].get_text())
    # print(primaryWeaponsData[weapon+14].get_text())


    # pWeapon.append(weapon[0], weapon[1], weapon[2], weapon[3])
    i = 0
    # for i in range(13):
    #     print(weapon)

# for x in range(0,12):
#     print(dataArsenal[x].get_text())


# print(dataArsenal.get_text())

