import csv

# Open the 'data.txt' file in read mode and read the data into a string
with open('data.txt', 'r') as file:
    data = file.read()

# Split the string into a list of rows
rows = data.split('\n')
# Create a CSV reader object to iterate over the rows in the list
reader = csv.reader(rows)

total = 0

startingPositions = {
    1: ['F', 'C', 'P', 'G', 'Q', 'R'],
    2: ['W', 'T', 'C', 'P'],
    3: ['B', 'H', 'P', 'M', 'C'],
    4: ['L', 'T', 'Q', 'S', 'M', 'P', 'R'],
    5: ['P', 'H', 'J', 'Z', 'V', 'G', 'N'],
    6: ['D','P','J'],
    7: ['L', 'G', 'P', 'Z', 'F', 'J', 'T', 'R'],
    8: ['N', 'L', 'H', 'C', 'F', 'P', 'T', 'J'],
    9: ['G', 'V', 'Z', 'Q', 'H', 'T', 'C', 'W'],
}

def moveBoxes(numberToMove, moveFrom, moveTo):
    for i in range(0, numberToMove, 1):
        movingBox = startingPositions[moveFrom].pop(-1)
        startingPositions[moveTo].append(movingBox)
    return startingPositions
        
def topBoxes():
    code = ''
    for row in startingPositions:
        code += startingPositions[row][-1]
    print(code)

for row in reader:
    directions = row[0].split(' ')
    numberToMove = int(directions[1])
    moveFrom = int(directions[3])
    moveTo = int(directions[5])
    # print(numberToMove, moveFrom, moveTo)
    moveBoxes(numberToMove, moveFrom, moveTo)

topBoxes()