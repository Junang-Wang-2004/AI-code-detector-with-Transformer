# Time:  O(n)
# Space: O(1)
from collections import Counter


class Solution2(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        """
        counter = Counter()
        left, max_length = 0, 0
        for right, char in enumerate(s):
            counter[char] += 1
            while len(counter) > k:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            max_length = max(max_length, right-left+1)
        return max_length
