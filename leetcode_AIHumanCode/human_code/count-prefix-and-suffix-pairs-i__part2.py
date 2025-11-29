# Time:  O(n^2 * l)
# Space: O(1)
# brute force
class Solution2(object):
    def countPrefixSuffixPairs(self, words):
        """
        """
        def check(i, j):
            return words[j].startswith(words[i]) and words[j].endswith(words[i])
    
        return sum(check(i, j) for i in range(len(words)) for j in range(i+1, len(words)))
