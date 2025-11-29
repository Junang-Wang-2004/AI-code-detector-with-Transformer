class Solution:
    def canBeTypedWords(self, text, brokenLetters):
        invalid = set(brokenLetters)
        count = 0
        for word in text.split():
            if all(char not in invalid for char in word):
                count += 1
        return count
