class Solution:
    def firstPalindrome(self, words):
        for term in words:
            backward = ""
            for letter in term:
                backward = letter + backward
            if term == backward:
                return term
        return ""
