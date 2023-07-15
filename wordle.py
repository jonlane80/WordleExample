import wordlist
import guessChecker
from guessPrinter import printGuesses
from colorama import Fore

def loadWord():
    words = wordlist.WordFile("./data/wordlist.json")
    return words.getWord()

def getUserGuess(number):
    return input ("Enter guess " + str(number) + ": ")

maxGuesses = 5
word = loadWord()["word"]
checker = guessChecker.GuessChecker(word)
# print ("guessing: " + word)
pastGuesses = []
correct = {}
# Make it (maxzGuesses + 1) since the range is up to but not including
for guessNumber in range(1, maxGuesses+1):
    guess = getUserGuess(guessNumber)
    correct = checker.checkGuess(guess)
    pastGuesses.append(correct)

    printGuesses(pastGuesses)
    
    if correct["result"]:
        print ("Guessed Correctly in %1d guess" % guessNumber, end='')
        print( "es" if guessNumber > 1 else '')
        break

if not correct["result"]:
    print ("\nBetter luck next time. The word was")
    print (Fore.GREEN, word)
    print (Fore.WHITE, "", end='')