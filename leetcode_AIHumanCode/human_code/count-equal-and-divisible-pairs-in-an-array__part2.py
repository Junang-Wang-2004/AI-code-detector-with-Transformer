# Time:  O(nlogk + n * sqrt(k)^2) = O(n * k)
# Space: O(n * sqrt(k)), number of factors of k is at most sqrt(k)
import collections


# math, number theory
class Solution2(object):
    def countPairs(self, nums, k):
        """
        """
        def gcd(x, y):
            while y:
                x, y = y, x%y
            return x
    
        cnts = collections.defaultdict(collections.Counter)
        for i, x in enumerate(nums):
            cnts[x][gcd(i, k)] += 1
        result = 0
        for cnt in cnts.values():
            for x in cnt.keys():
                for y in cnt.keys():
                    if x > y or x*y%k:
                        continue
                    result += cnt[x]*cnt[y] if x != y else cnt[x]*(cnt[x]-1)//2
        return result


