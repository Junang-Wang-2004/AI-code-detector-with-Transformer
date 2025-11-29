class Solution:
    def longestWord(self, words):
        word_set = set(words)
        candidates = sorted(words, key=lambda w: (-len(w), w))
        for word in candidates:
            if all(word[:i + 1] in word_set for i in range(len(word))):
                return word
        return ""
