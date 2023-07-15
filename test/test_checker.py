
import guessChecker

def test_checker():
    checker = guessChecker.GuessChecker("test")
    assert(checker.checkGuess("test")["result"])
    assert not(checker.checkGuess("blah")["result"])

def test_position():
    checker = guessChecker.GuessChecker("abcde")
    result = checker.checkGuess("acpoit")
    assert not (result["result"])
    assert (result["characters"][0]["positionCorrect"])
    assert (result["characters"][0]["characterExists"])
    assert not (result["characters"][1]["positionCorrect"])
    assert (result["characters"][1]["characterExists"])
    assert not (result["characters"][2]["positionCorrect"])
    assert not (result["characters"][2]["characterExists"])
    assert not (result["characters"][3]["positionCorrect"])
    assert not (result["characters"][3]["characterExists"])
    assert not (result["characters"][4]["positionCorrect"])
    assert not (result["characters"][4]["characterExists"])
    assert not (result["characters"][5]["positionCorrect"])
    assert not (result["characters"][5]["characterExists"])