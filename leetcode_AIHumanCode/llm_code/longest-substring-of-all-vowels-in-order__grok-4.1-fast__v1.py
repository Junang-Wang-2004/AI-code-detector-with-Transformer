class Solution:
    def longestBeautifulSubstring(self, word):
        ans = 0
        clen = 1
        dist = 1
        for j in range(1, len(word)):
            if word[j] < word[j - 1]:
                clen = 1
                dist = 1
            else:
                clen += 1
                if word[j] > word[j - 1]:
                    dist += 1
            if dist == 5:
                ans = max(ans, clen)
        return ans
