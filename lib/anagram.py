# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word

    @property
    def word(self):
        return self._word

    @word.setter
    def word(self, word):
        if isinstance(word, str):
            self._word = word
        else:
            print("word must be a string")

    def match(self, candidates):
        sorted_word = sorted(self.word)
        return [candidate for candidate in candidates if sorted(candidate) == sorted_word]