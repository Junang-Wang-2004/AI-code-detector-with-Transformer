class Solution:
    def possibleStringCount(self, word):
        matches = 0
        for left, right in zip(word, word[1:]):
            if left == right:
                matches += 1
        return matches + 1
