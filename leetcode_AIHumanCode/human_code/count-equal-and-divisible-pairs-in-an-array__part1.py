# Time:  O(nlogk + n * sqrt(k))
# Space: O(n + sqrt(k)), number of factors of k is at most sqrt(k)

import collections


# math, number theory
class Solution(object):
    def countPairs(self, nums, k):
        """
        """
        def gcd(x, y):
            while y:
                x, y = y, x%y
            return x
    
        idxs = collections.defaultdict(list)
        for i, x in enumerate(nums):
            idxs[x].append(i)
        result = 0
        for idx in idxs.values():
            gcds = collections.Counter()
            for i in idx:
                gcd_i = gcd(i, k)
                result += sum(cnt for gcd_j, cnt in gcds.items() if gcd_i*gcd_j%k == 0)
                gcds[gcd_i] += 1
        return result


