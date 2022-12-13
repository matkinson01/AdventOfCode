
with open('data.txt', 'r') as file:
    data = file.read()

letters = [*data]
    
for i in range(0, len(letters) - 4, 1):
    checking = letters[i:i+4]
    uniqueList = []

    for letter in checking:
        if(letter not in uniqueList):
            uniqueList.append(letter)
    
    if(checking == uniqueList):
        print(i+4, checking, uniqueList)

        break
        
    

