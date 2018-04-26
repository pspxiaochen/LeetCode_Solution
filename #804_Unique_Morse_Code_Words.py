def uniqueMorseRepresentations(words):
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    res = []
    for word in words:
        wordMorse = ""
        for s in word:
            wordMorse += morse[ord(s) - 97]
        res.append(wordMorse)
    return len(set(res))
