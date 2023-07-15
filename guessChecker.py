
class GuessChecker:
    def __init__(self, word):
        self.word = word

    def checkGuess(self, guess):
        guessResult = {}
        guessResult["result"] = (guess == self.word)
        guessResult["characters"] = self.checkCharacters(guess)
        return guessResult

    def checkCharacters(self, guess):
        charList = list(guess)
        charWord = list(self.word)
        i = 0
        results = []
        for char in charList:
            result = {}
            result["positionCorrect"] = len(charWord) > i and charWord[i] == char
            result["characterExists"] = char in charWord
            result["character"] = char
            results.append(result)
            i+=1
        return results