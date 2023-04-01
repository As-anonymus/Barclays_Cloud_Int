import requests
from bs4 import BeautifulSoup
import csv

# Define the URL to scrape
url = 'https://www.kaggle.com/datasets/krantiswalke/bankfullcsv'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

data = []
table = soup.find('table') # assuming there is a table on the webpage
rows = table.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    data.append(cols)

# Save the data to a CSV file
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)



