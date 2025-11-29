# Time:  O(n)
# Space: O(1)

import collections


# freq table, edge cases
class Solution(object):
    def equalFrequency(self, word):
        """
        """
        cnt = collections.Counter(iter(collections.Counter(word).values()))
        if len(cnt) > 2:
            return False
        if len(cnt) == 1:
            a = list(cnt.keys())[0]
            return a == 1 or cnt[a] == 1
        a, b = list(cnt.keys())
        if a > b:
            a, b = b, a
        return (a == 1 and cnt[a] == 1) or (a+1 == b and cnt[b] == 1)


