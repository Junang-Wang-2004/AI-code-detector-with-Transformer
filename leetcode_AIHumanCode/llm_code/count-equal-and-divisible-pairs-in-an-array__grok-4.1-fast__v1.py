import collections

class Solution(object):
    def countPairs(self, nums, k):
        divisors = []
        i = 1
        while i * i <= k:
            if k % i == 0:
                divisors.append(i)
                if i != k // i:
                    divisors.append(k // i)
            i += 1
        divisors.sort()
        
        pos_by_val = collections.defaultdict(list)
        for j, num in enumerate(nums):
            pos_by_val[num].append(j)
        
        ans = 0
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        for positions in pos_by_val.values():
            counts = {d: 0 for d in divisors}
            for p in positions:
                g = gcd(p, k)
                m = k // g
                ans += counts.get(m, 0)
                for d in divisors:
                    if p % d == 0:
                        counts[d] += 1
        return ans
