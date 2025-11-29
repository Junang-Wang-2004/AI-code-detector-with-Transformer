# Time:  O(n), x = len(KMP(s, a)), y = len(KMP(s, b))
# Space: O(min(a + b + x + y, n))

# kmp, two pointers
class Solution(object):
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
            prefix = getPrefix(pattern)
            j = -1
            for i in range(len(text)):
                while j+1 > 0 and pattern[j+1] != text[i]:
                    j = prefix[j]
                if pattern[j+1] == text[i]:
                    j += 1
                if j+1 == len(pattern):
                    yield i-j
                    j = prefix[j]

        result = []
        if not (len(a) <= len(s) and len(b) <= len(s)):
            return result
        lookup = list(KMP(s, b))
        j = 0
        for i in KMP(s, a):
            while j < len(lookup) and lookup[j] < i-k:
                j += 1
            if j < len(lookup) and lookup[j] <= i+k:
                result.append(i)
        return result


