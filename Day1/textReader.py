import csv

with open('data.txt', 'r') as file:
    data = file.read()

rows = data.split('\n')

reader = csv.reader(rows)

currentValue = 0
highestValue = 0
secondHighestValue = 0
thirdHighestValue = 0

for row in reader:
    if row != []:
        for field in row:
            currentValue += int(field)
    else : 
        if currentValue > thirdHighestValue:
            if currentValue > secondHighestValue:
                if currentValue > highestValue:
                    thirdHighestValue = secondHighestValue
                    secondHighestValue = thirdHighestValue
                    highestValue = currentValue
                else: 
                    thirdHighestValue = secondHighestValue
                    secondHighestValue = currentValue
            else: 
                thirdHighestValue = currentValue
        currentValue = 0
print(highestValue + secondHighestValue + thirdHighestValue)