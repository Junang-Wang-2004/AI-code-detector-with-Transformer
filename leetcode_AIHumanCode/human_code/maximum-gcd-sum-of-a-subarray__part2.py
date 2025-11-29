# Time:  O(nlogr), r = max(nums)
# Space: O(n)
# number theory, dp, prefix sum
class Solution2(object):
    def maxGcdSum(self, nums, k):
        """
        """
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        prefix = [0]*(len(nums)+1)
        for i, x in enumerate(nums):
            prefix[i+1] = prefix[i]+x
        result = 0
        dp = []
        for right, x in enumerate(nums):
            dp.append((right, x))
            new_dp = []
            for left, g in dp:  # Time: O(logr)
                ng = gcd(g, x)  # Total Time: O(nlogr)
                if not new_dp or new_dp[-1][1] != ng:
                    new_dp.append((left, ng))  # left and ng are both strictly increasing
            dp = new_dp
            for left, g in dp:
                if right-left+1 < k:
                    break
                result = max(result, (prefix[right+1]-prefix[left])*g)
        return result


