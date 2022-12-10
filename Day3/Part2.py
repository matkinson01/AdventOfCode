import csv

# Open the 'data.txt' file in read mode and read the data into a string
with open('data.txt', 'r') as file:
    data = file.read()

# Split the string into a list of rows
rows = data.split('\n')
# Create a CSV reader object to iterate over the rows in the list
reader = csv.reader(rows)

# Define a dictionary containing the letter-prioritized values of each letter in the English alphabet
letterPrioritizedValues = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
    'A': 27,
    'B': 28,
    'C': 29,
    'D': 30,
    'E': 31,
    'F': 32,
    'G': 33,
    'H': 34,
    'I': 35,
    'J': 36,
    'K': 37,
    'L': 38,
    'M': 39,
    'N': 40,
    'O': 41,
    'P': 42,
    'Q': 43,
    'R': 44,
    'S': 45,
    'T': 46,
    'U': 47,
    'V': 48,
    'W': 49,
    'X': 50,
    'Y': 51,
    'Z': 52
    }

# Initialize the total variable
total = 0

# Loop over the rows in groups of three (i.e. one group for each elf)
for i in range(0, len(rows), 3):
    elfGroup = rows[i:i+3]
    badge = 0

    # Loop over the items in each elf's rucksacks in groups of three
    for i in range(0, len(elfGroup), 3):
        # Create sets of items for each elf
        elf1 = set(elfGroup[i])
        elf2 = set(elfGroup[i+1])
        elf3 = set(elfGroup[i+2])

        # Find the items that are present in all three elf's rucksacks
        duplicate = elf1.intersection(elf2, elf3)
        # Join the duplicated items together into a string, look up the value in the dictionary 
        # and add it to the badge
        badge += letterPrioritizedValues["".join(duplicate)]
    
    # Add the value of the current elf's badge to the `total`
    total += badge
 # Print the total value of all the elves' badges
print(total)