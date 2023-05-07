from fernando import *
def arrayToString(array):
    filteredStr = "".join(str(i) for i in array)

    return filteredStr;
def convertBintoDec(bin1):
    soma = 0
    potencia = 0
    i = len(bin1) - 1
    while i >= 0:
        result = int((bin1[i]) * (2**potencia))
        soma += result
        potencia += 1
        i = i-1

    return soma;

def biggerBin(bin1, bin2):
    i = len(bin1)
    position = 0

    while position < i:
        if bin1[position] > bin2[position]:
            return "bin1";
        elif bin1[position] < bin2[position]:
            return "bin2";

        position+=1

    return "equal"

def borrow(subtractionResult, position):
    array = subtractionResult.copy()
    if array[position -1] == -1:
        borrow(array, position - 1)
    array[position -1] -= 1
    array[position] +=2

    return array

def subtraction(bin1, bin2):
    maior = biggerBin(bin1, bin2)

    if maior == "bin2":
        bigger = bin2
        smaller = bin1
    else:
        bigger = bin1
        smaller = bin2

    subtractionResult = []
    position = len(bin1) - 1

    for digits in range(len(bin1)):

        digitsSubtraction = bigger[position] - smaller[position]
        subtractionResult.insert(0, digitsSubtraction)
        position -= 1

    position = len(subtractionResult) - 1
    #print("num1: ", bin1)
    #print("num2: ", bin2)
    #print("Subtração direta: ", subtractionResult)
    for digits in range(len(subtractionResult)):
        if subtractionResult[position] < 0:
            subtractionResult = borrow(subtractionResult,position)
            #print(subtractionResult)
        position -= 1

    return subtractionResult

def convertBinToDecSM(bin1):
    sinal = bin1[0]
    filteredBin = bin1[1:]
    decSm = convertBintoDec(filteredBin)

    if sinal == 1:
        decSm = "-" + str(decSm)

    return decSm;



def subtractionsSM(userInput):
    bin1 = userInput[0]
    bin2 = userInput[1]

    sinalBin1 = bin1[0]
    sinalBin2 = bin2[0]
    filteredBin1 = bin1[1:]
    filteredBin2 = bin2[1:]

    maior = biggerBin(filteredBin1, filteredBin2)

    if sinalBin1 == 1:
         result = sumBin(filteredBin1,filteredBin2)

    else:
        result = subtraction(filteredBin1,filteredBin2)



    if (sinalBin1 == 1) or (maior == "bin2" and sinalBin2 == 1):
        result.insert(0, 1)
    else:
        result.insert(0,0)


    return result;

def sumBorrow(array,position):
    if array[position] == 2:
        array[position] = 1
        array[position - 1] += 1
        sumBorrow(array, (position -1))

    return array

def sumBin(bin1, bin2):
    position = 0
    sumResult = []
    for digits in range(len(bin1)):

        digitsSum = bin1[position] + bin2[position]
        sumResult.append(digitsSum)
        position += 1

    position = len(sumResult) -1
    for digits in range(len(sumResult)):

        if sumResult[position] == 2:
            sumResult[position] = 0
            if position - 1 >= 0:  #Evita somar um no último número em caso de overflow
                sumResult[position - 1] += 1

        elif sumResult[position] == 3:
            sumResult[position] = 1
            if position - 1 >= 0:  #Evita somar um no último número em caso de overflow
                sumResult[position - 1] += 1


        position -= 1


    return sumResult

def sumBinSm(bin1, bin2):
    sinalBin1 = bin1[0]
    sinalBin2 = bin2[0]
    filteredBin1 = bin1[1:]
    filteredBin2 = bin2[1:]

    maior = biggerBin(filteredBin1, filteredBin2)

    sumResult = sumBin(filteredBin1, filteredBin2)

    if (sinalBin1 or sinalBin2) == 1:
        sumResult = subtraction(filteredBin1, filteredBin2)

    if maior == "bin1":
        sumResult.insert(0, sinalBin1)
    else:
        sumResult.insert(0, sinalBin2)


    return sumResult;

def complementa2(bin1):

    if bin1[0] == 1:
        bin1 = complementa2Negative(bin1)


    return bin1;
def complementa2Negative(binario):
    position = 0;
    um = []

    for elemento in binario:
        if elemento == 0:
            binario[position] = 1
            um.append(0)
        else:
            binario[position] = 0
            um.append(0)
        position += 1


    lastPosition = len(um) -1
    um[lastPosition] = 1

    binC2MaisUm = sumBin(binario, um)

    return binC2MaisUm;

def c2ToDec(binario):

    negativo = False

    if binario[0] == 1:
        negativo = True
        binario = complementa2Negative(binario)

    binario = convertBintoDec(binario)

    if negativo == True:
        binario = "-" + str(binario)
    return binario;

def sumComplenta2(userInput):
    bin1 = userInput[0]
    bin2 = userInput[1]

    soma = sumBin(bin1, bin2)

    return soma;

def subtractionC2(userInput):
    bin1 = userInput[0]
    bin2 = userInput[1]

    if bin2[0] == 0:
        bin2 = complementa2Negative(bin2)

    soma = sumBin(bin1, bin2)

    return soma;
