# Time:  O(nlogr), r = max(nums)
# Space: O(n)
# bit manipulation, greedy, dp
class Solution3(object):
    def maximumStrongPairXor(self, nums):
        """
        """
        result = 0
        for i in reversed(range(max(nums).bit_length())):
            prefix_min, prefix_max = {}, {}
            for x in nums:
                y = x>>i
                if y not in prefix_min:
                    prefix_min[y] = prefix_max[y] = x
                prefix_min[y] = min(prefix_min[y], x)
                prefix_max[y] = max(prefix_max[y], x)
            result <<= 1
            for x in prefix_min.keys():
                y = (result|1)^x
                assert(x != y)
                if y in prefix_max and prefix_min[max(x, y)] <= 2*prefix_max[min(x, y)]:
                    result |= 1
                    break
        return result
