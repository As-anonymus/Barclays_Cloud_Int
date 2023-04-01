import csv
import json

with open('BankCustomerData.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]

with open('BankCustomerData.json', 'w') as file:
    json.dump(data, file)