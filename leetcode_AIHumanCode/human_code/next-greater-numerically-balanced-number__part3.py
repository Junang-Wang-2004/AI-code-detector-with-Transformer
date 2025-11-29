# Time:  O(l * c) = O(1), c is the count of all balanced's permutations, l is the max length of permutations
# Space: O(l * b) = O(1), b is the count of balanced
import itertools


class Solution3(object):
    def nextBeautifulNumber(self, n):
        """
        """
        # obtained by manually enumerating min number of permutations in each length
        balanced = [1,
                    22,
                    122, 333,
                    1333, 4444,
                    14444, 22333, 55555,
                    122333, 155555, 224444, 666666]
        s = tuple(str(n))
        result = 1224444
        for x in balanced:
            x = tuple(str(x))
            if len(x) < len(s):
                continue
            if len(x) > len(s):
                result = min(result, int("".join(x)))
                continue
            for perm in itertools.permutations(x):  # not distinct permutations
                if perm > s:
                    result = min(result, int("".join(perm)))
        return result
