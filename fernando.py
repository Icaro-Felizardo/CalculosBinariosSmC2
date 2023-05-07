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


def sumBinFernando(bin1, bin2):
    overflow = 0
    somaBinario = []
    numSum = 0
    for i in range(len(bin1)):
        numSum = bin1[-(i + 1)] + bin2[-(i + 1)] + overflow
        if numSum <= 1:
            somaBinario.insert(0, numSum)
            overflow = 0
        else:
            somaBinario.insert(0, (numSum % 2))
            overflow += 1
    if overflow > 0:
        somaBinario.insert(0, overflow)
    return somaBinario


# archiveName = input("Digite o nome do arquivo: ");
archiveName = "teste.txt"

userInput = readUserInput(archiveName)
userInput = formatUserInput(userInput)
#somaBin = sumBin(userInput[0], userInput[1])


def main():
    # if len(userInput[1]) != len(userInput[0]) and len(userInput[1])<32 or len(userInput[0])<32:
    #     print("Seus números não possui 32 bits ou possuem tamanhos diferentes. Mude o arquivo e tente novamente")
    # else:
    print(userInput)
    #print(somaBin)


#main()