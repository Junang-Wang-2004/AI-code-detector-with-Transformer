class Solution:
    def mergeAlternately(self, word1, word2):
        ln = min(len(word1), len(word2))
        ans = ''.join(word1[k] + word2[k] for k in range(ln))
        if len(word1) > len(word2):
            ans += word1[ln:]
        else:
            ans += word2[ln:]
        return ans
