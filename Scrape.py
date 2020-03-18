from bs4 import BeautifulSoup
import requests
from Mail import sendMail
from writeAndRead import saveData, checkData

data = 0
source = requests.get('https://www.worldometers.info/coronavirus/').text
soup = BeautifulSoup(source, 'html.parser')
table = soup.find('tbody')
i = 3
for row in table.find_all_next(string=True):
    i = i + 1
    if 'Denmark' in row:
        i = 0
    if i == 2:
        data = row
        break


data = int((str(data).replace(',', '')))

if data > checkData():
    print('Sending email')
    sendMail(data)
    print('Saving data')
    saveData(str(data))


