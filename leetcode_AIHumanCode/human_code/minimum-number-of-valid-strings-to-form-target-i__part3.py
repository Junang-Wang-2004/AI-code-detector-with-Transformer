# Time:  O(w * (l + n))
# Space: O(l + n)
# kmp, dp
class Solution3(object):
    def minValidStrings(self, words, target):
        """
        """
        def getPrefix(pattern):
            prefix = [-1]*len(pattern)
            j = -1
            for i in range(1, len(pattern)):
                while j+1 > 0 and pattern[j+1] != pattern[i]:
                    j = prefix[j]
                if pattern[j+1] == pattern[i]:
                    j += 1
                prefix[i] = j
            return prefix

        def KMP(text, pattern, callback):
            prefix = getPrefix(pattern)
            j = -1
            for i in range(len(text)):
                while j+1 > 0 and pattern[j+1] != text[i]:
                    j = prefix[j]
                if pattern[j+1] == text[i]:
                    j += 1
                callback(i, j)
                if j+1 == len(pattern):
                    j = prefix[j]

        def update(i, j):
            lookup[i] = max(lookup[i], j+1)

        lookup = [0]*len(target)
        for w in words:
            KMP(target, w, update)
        dp = [0]*(len(target)+1)
        for i in range(len(target)):
            if not lookup[i]:
                return -1
            dp[i+1] = dp[(i-lookup[i])+1]+1
        return dp[-1]


