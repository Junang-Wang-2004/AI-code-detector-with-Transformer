# Time:  O(q * n * l)
# Space: O(1)
import itertools


# brute force
class Solution2(object):
    def twoEditWords(self, queries, dictionary):
        """
        """
        return [q for q in queries if any(sum(c1 != c2 for c1, c2 in zip(q, d)) <= 2 for d in dictionary)]
