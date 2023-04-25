from icaro import *

#archiveName = input("Digite o nome do arquivo: ");
archiveName = "teste.txt"

userInput = readUserInput(archiveName)
userInput = formatUserInput(userInput)
subtraction = subtractionSM(userInput[0], userInput[1])
