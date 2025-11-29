# Time:  O(n * 2^n) ~ O((n * 2^n)^2)
# Space: O(1)
class Solution2(object):
    def subsetsWithDup(self, nums):
        """
        """
        result = []
        i, count = 0, 1 << len(nums)
        nums.sort()

        while i < count:
            cur = []
            for j in range(len(nums)):
                if i & 1 << j:
                    cur.append(nums[j])
            if cur not in result:
                result.append(cur)
            i += 1

        return result


