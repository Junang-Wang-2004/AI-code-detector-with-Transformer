# Time:  O(m * n), m is the number of words, n is the length of each word
# Space: O(n)
import collections


# freq table
class Solution2(object):
    def oddString(self, words):
        """
        """
        cnt = collections.Counter(tuple(ord(w[i+1])-ord(w[i]) for i in range(len(w)-1)) for w in words)
        target = next(k for k, v in cnt.items() if v == 1)
        return next(w for w in words if tuple(ord(w[i+1])-ord(w[i]) for i in range(len(w)-1)) == target)
