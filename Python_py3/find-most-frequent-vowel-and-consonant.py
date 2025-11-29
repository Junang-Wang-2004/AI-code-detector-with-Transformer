# Time:  O(n + 26)
# Space: O(26)

# freq table
class Solution(object):
    def maxFreqSum(self, s):
        """
        """
        VOWELS = {'a', 'e', 'i', 'o', 'u'}
        cnt = [0]*26
        for x in s:
            cnt[ord(x)-ord('a')] += 1
        return max(cnt[i] for i in range(26) if chr(i+ord('a')) in VOWELS)+\
               max(cnt[i] for i in range(26) if chr(i+ord('a')) not in VOWELS)
