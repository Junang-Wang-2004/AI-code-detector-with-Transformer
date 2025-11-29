import collections
import math

class Solution:
    def countPairs(self, nums, k):
        freq = collections.Counter(math.gcd(num, k) for num in nums)
        divisors = list(freq)
        res = 0
        m = len(divisors)
        for i in range(m):
            da = divisors[i]
            for j in range(i, m):
                db = divisors[j]
                if (da * db) % k == 0:
                    if i == j:
                        res += freq[da] * (freq[da] - 1) // 2
                    else:
                        res += freq[da] * freq[db]
        return res
