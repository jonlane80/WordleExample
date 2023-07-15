# TODO: Constructor to load the file
# TODO: Method to return a random word
import json
import random

class WordFile:
    def __init__(self, filename):
        file = open (filename)
        self.wordlist = json.load(file)
    def getWord(self):
        wordNumber = random.randint(0, len(self.wordlist) - 1)
        return self.wordlist[wordNumber]