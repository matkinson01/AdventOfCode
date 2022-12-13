import csv

# Open the 'data.txt' file in read mode and read the data into a string
with open('data.txt', 'r') as file:
    data = file.read()

# Split the string into a list of rows
rows = data.split('\n')
# Create a CSV reader object to iterate over the rows in the list
reader = csv.reader(rows)

total = 0

for row in reader:
    firstElf = row[0].split('-')
    secondElf = row[1].split('-')

    firstLow = int(firstElf[0])
    firstHigh = int(firstElf[1])
    secondLow = int(secondElf[0])
    secondHigh = int(secondElf[1])

    # In this case we are checking if the low value from either range falls within the other
    # if it does, we add 1 to the count total
    if(firstLow >= secondLow):
        if(firstLow <= secondHigh):
            total += 1
    elif(secondLow >= firstLow):
        if(secondLow <= firstHigh):
            total += 1
    
print(total)