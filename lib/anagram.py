# lib/anagram.py

class Anagram:

    def __init__(self, word):
        self.word = sorted(word.lower())

    def match(self, candidate):
        result = []

        for w in candidate:
            lw = w.lower()
            if sorted(lw) == self.word:
                result.append(lw)
        return result






