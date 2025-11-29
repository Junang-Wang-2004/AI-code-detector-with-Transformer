# Time:  O(n)
# Space: O(1)
# array
class Solution2(object):
    def minimumCost(self, nums):
        """
        """
        def topk(a, k):
            result = [float("inf")]*k
            for x in a:
                for i in range(len(result)):
                    if x < result[i]:
                        result[i], x = x, result[i]
            return result

        return nums[0]+sum(topk((nums[i] for i in range(1, len(nums))), 2))
