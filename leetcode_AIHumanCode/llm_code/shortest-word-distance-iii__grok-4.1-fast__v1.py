class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        ans = float('inf')
        prev1 = prev2 = -1
        if word1 == word2:
            for i, w in enumerate(words):
                if w == word1:
                    if prev1 > -1:
                        ans = min(ans, i - prev1)
                    prev1 = i
        else:
            for i, w in enumerate(words):
                if w == word1:
                    if prev2 > -1:
                        ans = min(ans, i - prev2)
                    prev1 = i
                elif w == word2:
                    if prev1 > -1:
                        ans = min(ans, i - prev1)
                    prev2 = i
        return ans
