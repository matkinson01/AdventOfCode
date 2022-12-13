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

    # If the fist set falls within the second the firstLow will be >=0 and the firstHigh will be <=0
    # If the second set falls within the first the secondLow will be >=0 and the secondHigh will be <=0
    # Using that logic if the low difference and the high difference are opposites (one is + the other is -)
    # then one set will fall within the other
    # i.e. 1-15 & 3-9
    #      1-3 = -2
    #      15-9 = 6
    lowDifference = firstLow - secondLow
    highDifference = firstHigh - secondHigh

    if(
        (lowDifference <= 0 and highDifference >= 0) or 
        (lowDifference >= 0 and highDifference <= 0)
    ):
        total += 1
    
print(total)