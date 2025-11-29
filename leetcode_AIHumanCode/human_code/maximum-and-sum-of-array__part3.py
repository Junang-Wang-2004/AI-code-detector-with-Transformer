# Time:  O(n * 3^n)
# Space: O(3^n)
# bottom-up dp (hard to implement but faster)
class Solution3(object):
    def maximumANDSum(self, nums, numSlots):
        """
        """
        def count(x):
            result = 0
            while x:
                result += x%3
                x //= 3
            return result

        dp = [0]*(3**numSlots)
        for mask in range(1, len(dp)):
            i = count(mask)-1
            x = nums[i] if i < len(nums) else 0
            base = 1
            for slot in range(1, numSlots+1):
                if mask//base%3:
                    dp[mask] = max(dp[mask], (x&slot)+dp[mask-base])
                base *= 3
        return dp[-1]


