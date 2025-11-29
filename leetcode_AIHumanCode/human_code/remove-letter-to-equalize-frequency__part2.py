# Time:  O(26 * n)
# Space: O(1)
import collections


# brute force, freq table
class Solution2(object):
    def equalFrequency(self, word):
        """
        """
        cnt = collections.Counter(collections.Counter(word))
        for c in word:
            cnt[c] -= 1
            if len(collections.Counter(c for c in cnt.values() if c)) == 1:
                return True
            cnt[c] += 1
        return False
