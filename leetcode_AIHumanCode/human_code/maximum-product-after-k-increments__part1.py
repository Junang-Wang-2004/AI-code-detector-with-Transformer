# Time:  O(nlogn)
# Space: O(1)

# math, sort
class Solution(object):
    def maximumProduct(self, nums, k):
        """
        """
        MOD = 10**9+7
        nums.sort()
        total = sum(nums)
        for i in reversed(range(len(nums))):
            if nums[i]*(i+1)-total <= k:
                break
            total -= nums[i]
        q, r = divmod(k+total, i+1)
        return (pow(q, (i+1)-r, MOD)*pow(q+1, r, MOD)*
                reduce(lambda x, y: x*y%MOD, (nums[j] for j in range(i+1, len(nums))), 1)) % MOD


