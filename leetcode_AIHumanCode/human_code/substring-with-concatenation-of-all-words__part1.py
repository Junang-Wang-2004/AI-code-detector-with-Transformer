# Time:  O((m + n) * k), where m is string length, n is dictionary size, k is word length
# Space: O(n * k)

import collections


class Solution(object):
    def findSubstring(self, s, words):
        """
        """
        if not words:
            return []

        result, m, n, k = [], len(s), len(words), len(words[0])
        if m < n*k:
            return result

        lookup = collections.defaultdict(int)
        for i in words:
            lookup[i] += 1                # Space: O(n * k)

        for i in range(k):               # Time:  O(k)
            left, count = i, 0
            tmp = collections.defaultdict(int)
            for j in range(i, m-k+1, k): # Time:  O(m / k)
                s1 = s[j:j+k]             # Time:  O(k)
                if s1 in lookup:
                    tmp[s1] += 1
                    count += 1
                    while tmp[s1] > lookup[s1]:
                        tmp[s[left:left+k]] -= 1
                        count -= 1
                        left += k
                    if count == n:
                        result.append(left)
                else:
                    tmp = collections.defaultdict(int)
                    count = 0
                    left = j+k
        return result


