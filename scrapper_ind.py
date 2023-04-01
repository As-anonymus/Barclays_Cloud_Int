import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
import sqlite3
conn=sqlite3.connect('toll_data.db')
#c=conn.cursor()

r = requests.get('https://www.kaggle.com/datasets/krantiswalke/bankfullcsv')

soup = BeautifulSoup(r.text, 'html.parser')

plaza_name = soup.find(class_='PA15').find_all('p')[0].find('lable')

table = soup.find_all('table',class_='tollinfotbl')[0]

x = str(table)

y = pd.read_html(x)[0].dropna(axis=0,how='all')

cols = y.columns.tolist()

cols.insert(0,'Date Scrapped')

cols.insert(1,'Plaza Name')

y['Plaza Name' ] = plaza_name.text

y['Date Scrapped'] = date.today() 

y = y[cols]

y.to_sql('toll_data',conn,if_exists='append',index=False)

print(table)