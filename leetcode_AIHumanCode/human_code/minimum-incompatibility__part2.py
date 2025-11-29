# Time:  O(max(n * 2^n, 3^n))
# Space: O(2^n)
class Solution_TLE(object):
    def minimumIncompatibility(self, nums, k):
        """
        """
        inf = (len(nums)-1)*(len(nums)//k)+1
        POW = [1]
        for i in range(len(nums)):
            POW.append(POW[-1]<<1)
        
        def popcount(n):
            result = 0
            while n:
                n &= n - 1
                result += 1
            return result
    
        def find_candidates(nums, k):
            total = POW[len(nums)]-1
            m = len(nums)//k
            result = [inf]*(total+1)
            for mask in range(total+1):
                if popcount(mask) != m:
                    continue
                lookup = 0
                mx, mn = 0, inf
                for i in range(len(nums)):
                    if mask&POW[i] == 0:
                        continue
                    if lookup&POW[nums[i]]:
                        break
                    lookup |= POW[nums[i]]
                    mx = max(mx, nums[i])
                    mn = min(mn, nums[i])
                else:
                    result[mask] = mx-mn
            return result
        
        candidates = find_candidates(nums, k)
        m = len(nums)//k
        total = POW[len(nums)]-1
        dp = [inf]*(total+1)
        dp[0] = 0
        for mask in range(total+1):
            if popcount(mask) % m != 0:
                continue
            # submask enumeration:
            # => sum(nCr(n, k) * 2^k for k in xrange(n+1)) = (1 + 2)^n = 3^n
            # => Time: O(3^n), see https://cp-algorithms.com/algebra/all-submasks.html
            submask = mask
            while submask:
                dp[mask] = min(dp[mask], dp[mask-submask] + candidates[submask])
                submask = (submask-1)&mask
        return dp[-1] if dp[-1] != inf else -1


