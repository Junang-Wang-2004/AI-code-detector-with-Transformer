from functools import reduce
# Time:  O(n + r), r = max(nums)
# Space: O(n + r)

# combinatorics, stars and bars
class Solution(object):
    def countOfPairs(self, nums):
        """
        """
        fact, inv, inv_fact = [[1]*2 for _ in range(3)]
        def nCr(n, k):
            while len(inv) <= n:  # lazy initialization
                fact.append(fact[-1]*len(inv) % MOD)
                inv.append(inv[MOD%len(inv)]*(MOD-MOD//len(inv)) % MOD)  # https://cp-algorithms.com/algebra/module-inverse.html
                inv_fact.append(inv_fact[-1]*inv[-1] % MOD)
            return (fact[n]*inv_fact[n-k] % MOD) * inv_fact[k] % MOD
    
        def nHr(n, r):
            return nCr(n+r-1, r)

        MOD = 10**9+7
        # arr1 = [0+x1, arr1[0]+max(nums[1]-nums[0], 0)+x2, ..., arr[n-2]+max(nums[n-1]-nums[n-2], 0)+xn]
        # => sum(max(nums[i]-nums[i-1], 0) for i in xrange(1, len(nums)))+(x1+x2+...+xn) <= nums[-1]
        # => x1+x2+...+xn <= nums[-1]-sum(max(nums[i]-nums[i-1], 0) for i in xrange(1, len(nums))) = cnt <= min(nums)
        # => the answer is the number of solutions s.t. x1+x2+...+xn <= cnt, where cnt >= 0
        cnt = nums[-1]-sum(max(nums[i]-nums[i-1], 0) for i in range(1, len(nums)))
        return nHr(len(nums)+1, cnt) if cnt >= 0 else 0
    

