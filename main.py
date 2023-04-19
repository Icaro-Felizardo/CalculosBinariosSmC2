def readUserInput(archiveName):
    userInput = open(archiveName).readlines()
    filteredUserInput = []
    for i in range(len(userInput)):
       filteredUserInput.append(userInput[i].strip())

    return filteredUserInput

def formatUserInput(filteredUserInput):
    finalList = []
    for i in range(len(filteredUserInput)):
        finalList.append(list(filteredUserInput[i]))
    return finalList


#archiveName = input("Digite o nome do arquivo: ");
archiveName = "teste.txt"

userInput = readUserInput(archiveName)
userInput = formatUserInput(userInput)




print(userInput)