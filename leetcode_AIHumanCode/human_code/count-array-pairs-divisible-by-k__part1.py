# Time:  O(nlogk + sqrt(k)^2) = O(nlogk + k)
# Space: O(sqrt(k)), number of factors of k is at most sqrt(k)

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
    
        cnt = collections.Counter()
        for x in nums:
            cnt[gcd(x, k)] += 1
        result = 0
        for x in cnt.keys():
            for y in cnt.keys():
                if x > y or x*y%k:
                    continue
                result += cnt[x]*cnt[y] if x != y else cnt[x]*(cnt[x]-1)//2
        return result


