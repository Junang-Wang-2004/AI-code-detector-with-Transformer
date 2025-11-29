# Time:  O(n)
# Space: O(n)
# KMP algorithm
class Solution2(object):
    def rotateString(self, A, B):
        """
        """
        def strStr(haystack, needle):
            def KMP(text, pattern):
                prefix = getPrefix(pattern)
                j = -1
                for i in range(len(text)):
                    while j > -1 and pattern[j + 1] != text[i]:
                        j = prefix[j]
                    if pattern[j + 1] == text[i]:
                        j += 1
                    if j == len(pattern) - 1:
                        return i - j
                return -1

            def getPrefix(pattern):
                prefix = [-1] * len(pattern)
                j = -1
                for i in range(1, len(pattern)):
                    while j > -1 and pattern[j + 1] != pattern[i]:
                        j = prefix[j]
                    if pattern[j + 1] == pattern[i]:
                        j += 1
                    prefix[i] = j
                return prefix

            if not needle:
                return 0
            return KMP(haystack, needle)

        if len(A) != len(B):
            return False
        return strStr(A*2, B) != -1


