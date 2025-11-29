# Time:  O(n * llogl)
# Space: O(l)
import collections


# sort
class Solution3(object):
    def removeAnagrams(self, words):
        """
        """
        return [words[i] for i in range(len(words)) if i == 0 or sorted(words[i-1]) != sorted(words[i])]
