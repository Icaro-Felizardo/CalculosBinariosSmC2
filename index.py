from functions import *
import sys



# for param in sys.argv:
#    archiveName = param

archiveName = "teste.txt"

userInput = readUserInput(archiveName)
userInput = formatUserInput(userInput)


dec1SM = convertBinToDecSM(userInput[0]);
print(dec1SM)

dec2SM = convertBinToDecSM(userInput[1]);
print(dec2SM)
print("")

sumSm = sumBinSm(userInput[0], userInput[1])
stringSumSm = arrayToString(sumSm)
print(stringSumSm)

subSm = subtractionsSM(userInput)
stringSubSm = arrayToString(subSm)
print(stringSubSm)
print("")

decSumSm = convertBinToDecSM(sumSm)
print(decSumSm)

decSubSm = convertBinToDecSM(subSm)
print(decSubSm)
print("")

dec1 = userInput[0].copy()
dec1C2 = c2ToDec(dec1)
print(dec1C2)

dec2 = userInput[1].copy()
dec2C2 = c2ToDec(dec2)
print(dec2C2)
print("")

sumC2 = sumComplenta2(userInput)
arraySumC2 = arrayToString(sumC2)
print(arraySumC2)

subC2 = subtractionC2(userInput)
arraySubC2 = arrayToString(subC2)
print(arraySubC2)
print("\n")

sumDecC2 = c2ToDec(sumC2)
print(sumDecC2)

subDecC2 = c2ToDec(subC2)
print(subDecC2)