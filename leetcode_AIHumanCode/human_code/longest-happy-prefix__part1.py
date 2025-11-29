# Time:  O(n)
# Space: O(n)

# kmp solution
class Solution(object):
    def longestPrefix(self, s):
        """
        """
        def getPrefix(pattern):
            prefix = [-1]*len(pattern)
            j = -1
            for i in range(1, len(pattern)):
                while j != -1 and pattern[j+1] != pattern[i]:
                    j = prefix[j]
                if pattern[j+1] == pattern[i]:
                    j += 1
                prefix[i] = j
            return prefix
        
        return s[:getPrefix(s)[-1]+1]


