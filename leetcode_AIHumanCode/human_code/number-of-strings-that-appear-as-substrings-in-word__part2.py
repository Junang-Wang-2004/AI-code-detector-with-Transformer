# Time:  O(n * (l + m)), n is the number of patterns
#                      , l is the max length of patterns
#                      , m is the length of word
# Space: O(l)
# kmp solution
class Solution2(object):
    def numOfStrings(self, patterns, word):
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
            
        def kmp(text, pattern):
            if not pattern:
                return 0
            prefix = getPrefix(pattern)
            if len(text) < len(pattern):
                return -1
            j = -1
            for i in range(len(text)):
                while j != -1 and pattern[j+1] != text[i]:
                    j = prefix[j]
                if pattern[j+1] == text[i]:
                    j += 1
                if j+1 == len(pattern):
                    return i-j
            return -1
        
        return sum(kmp(word, pattern) != -1 for pattern in patterns)


