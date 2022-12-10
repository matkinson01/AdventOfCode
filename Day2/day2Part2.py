import csv

with open('data.txt', 'r') as file:
    data = file.read()

rows = data.split('\n')

reader = csv.reader(rows)

results = {
    'BX': 1, 
    'CX': 2, 
    'AX': 3, 
    'AY': 4, 
    'BY': 5, 
    'CY': 6, 
    'CZ': 7, 
    'AZ': 8, 
    'BZ': 9
    }

total = 0

for row in reader:
    for field in row:
        total += results[field]

print(total)