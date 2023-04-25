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
    for j in range(len(finalList)):
        for i in range(0, len(finalList[j])):
            finalList[j][i] = int(finalList[j][i])
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

def borrow(subtractionResult, position):
    array = subtractionResult.copy()
    if array[position -1] == -1:
        borrow(array, position - 1)
    array[position -1] -= 1
    array[position] +=2

    return array

def subtractionSM(binNumber1, binNumber2):
    subtractionResult = []
    position = len(binNumber1) - 1

    for digits in range(len(binNumber1) - 1):

        digitsSubtraction = binNumber1[position] - binNumber2[position]
        subtractionResult.insert(0, digitsSubtraction)
        position -= 1

    position = len(subtractionResult) - 1
    print("num1: ", binNumber1)
    print("num2: ", binNumber2)
    print("Subtração direta: ", subtractionResult)
    for digits in range(len(subtractionResult)):
        if subtractionResult[position] < 0:
            subtractionResult = borrow(subtractionResult,position)
            print(subtractionResult)
        position -= 1

    return subtractionResult
