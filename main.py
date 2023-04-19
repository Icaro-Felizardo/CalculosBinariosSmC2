def readUserInput(archiveName):
    userInput = open(archiveName).readlines()
    filteredUserInput = []
    for i in range(len(userInput)):
       filteredUserInput.append(userInput[i].strip())

    return filteredUserInput;
def stringInputToArray(oneInput):
    oneInputList = []
    for number in oneInput:
        oneInputList.append(number)
    return oneInputList;

def formatUserInput(filteredUserInput):
    finalList = []
    for i in range(len(filteredUserInput)):
        finalList.append(stringInputToArray(filteredUserInput[i]))
    return finalList

def convertBintoDecSEM(userInput):
    soma = 0
    i = len(userInput[0]) -1
    potencia = 0
    print(userInput[0])
    while i > 0:
        result = int((userInput[0][i]) * (2**potencia))
        print(userInput[0][i])
        print(result)
        soma = soma + result
        print(soma)
        potencia = potencia + 1
        i = i-1








#archiveName = input("Digite o nome do arquivo: ");
archiveName = "teste.txt"

userInput = readUserInput(archiveName)
userInput = formatUserInput(userInput)

decimal = convertBintoDecSEM(userInput)



print(decimal)