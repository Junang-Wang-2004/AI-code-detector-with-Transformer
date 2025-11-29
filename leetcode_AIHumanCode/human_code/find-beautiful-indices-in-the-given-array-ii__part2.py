# Time:  O(n + xlogy), x = len(KMP(s, a)), y = len(KMP(s, b))
# Space: O(n)
import bisect


# kmp, binary search
class Solution2(object):
    def beautifulIndices(self, s, a, b, k):
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

        def KMP(text, pattern):
            prefix = getPrefix(pattern+'#'+text)
            return ((i-(len(pattern)+1))-(len(pattern)-1) for i in range((len(pattern)+1)+(len(pattern)-1) , len(prefix)) if prefix[i]+1 == len(pattern))
    
        result = []
        if not (len(a) <= len(s) and len(b) <= len(s)):
            return result
        lookup = list(KMP(s, b))
        j = 0
        for i in KMP(s, a):
            j = bisect.bisect_left(lookup, i-k)
            if j < len(lookup) and lookup[j] <= i+k:
                result.append(i)
        return result
