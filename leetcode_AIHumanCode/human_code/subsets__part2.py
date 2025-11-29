# Time:  O(n * 2^n)
# Space: O(1)
class Solution2(object):
    def subsets(self, nums):
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
            result.append(cur)
            i += 1

        return result


