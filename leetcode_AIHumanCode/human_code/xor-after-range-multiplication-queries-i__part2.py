# Time:  O(q * n)
# Space: O(1)
# simulation
class Solution2(object):
    def xorAfterQueries(self, nums, queries):
        """
        """
        MOD = 10**9+7

        for l, r, k, v in queries:
            for i in range(l, r+1, k):
                nums[i] = (nums[i]*v)%MOD
        return reduce(lambda accu, x: accu^x, nums, 0)
