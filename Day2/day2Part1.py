import csv

# Open the data file, and store it in the data variable
with open('data.txt', 'r') as file:
    data = file.read()

rows = data.split('\n')

reader = csv.reader(rows)

# Results stores the expected value of a string combination in a 
#           dictionary. Each string result stored a interger value
#           that is the resut of us usinc that code.
#           I.E. A | X == "rock" == 1 point, a win = 6 points. So 
#           if you win with rock you get 7 points.
results = {
    'BX': 1, 
    'CY': 2, 
    'AZ': 3, 
    'AX': 4, 
    'BY': 5, 
    'CZ': 6, 
    'CX': 7, 
    'AY': 8, 
    'BZ': 9
    }

total = 0

for row in reader:
    for field in row:
        total += results[field]

print(total)