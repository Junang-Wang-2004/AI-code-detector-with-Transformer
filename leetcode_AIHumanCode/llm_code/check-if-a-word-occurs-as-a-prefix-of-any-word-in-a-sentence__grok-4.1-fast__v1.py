class Solution:
    def isPrefixOfWord(self, sentence, searchWord):
        words = sentence.split()
        for idx, term in enumerate(words, start=1):
            if term.startswith(searchWord):
                return idx
        return -1
