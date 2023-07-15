from colorama import Fore

def printGuesses(pastGuesses):
    for currentGuess in pastGuesses:
        printGuess(currentGuess)    
        print (Fore.WHITE, "")

def printGuess(currentGuess):
    for i in range(0, len(currentGuess["characters"])):
        colour = Fore.GREEN if currentGuess["characters"][i]["positionCorrect"] \
                            else Fore.YELLOW if currentGuess["characters"][i]["characterExists"] \
                            else Fore.RED
        print (colour, currentGuess["characters"][i]["character"], end='')