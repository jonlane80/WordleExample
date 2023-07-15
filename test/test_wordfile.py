import wordlist

def test_getword():
    words = wordlist.WordFile("./data/wordlist.json")
    word = words.getWord()
    assert (word is not None)
    assert (word != "")
    print ("word: " + word["word"])