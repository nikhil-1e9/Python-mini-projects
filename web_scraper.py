import requests
from bs4 import BeautifulSoup
import csv

url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

tables = soup.find_all('table')

data = []

for table in tables:
    rows = table.find_all('tr')
    for row in rows:
        cells = row.find_all('td')
        if len(cells) > 0:
            row_data = []
            for cell in cells:
                row_data.append(cell.text.strip())
            data.append(row_data)

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
