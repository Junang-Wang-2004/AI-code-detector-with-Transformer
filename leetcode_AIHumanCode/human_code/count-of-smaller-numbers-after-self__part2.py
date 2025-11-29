# Time:  O(nlogn)
# Space: O(n)
# BIT solution.
class Solution2(object):
    def countSmaller(self, nums):
        """
        """
        class BIT(object):  # 0-indexed.
            def __init__(self, n):
                self.__bit = [0]*(n+1)  # Extra one for dummy node.

            def add(self, i, val):
                i += 1  # Extra one for dummy node.
                while i < len(self.__bit):
                    self.__bit[i] += val
                    i += (i & -i)

            def query(self, i):
                i += 1  # Extra one for dummy node.
                ret = 0
                while i > 0:
                    ret += self.__bit[i]
                    i -= (i & -i)
                return ret

        # Get the place (position in the ascending order) of each number.
        sorted_nums = sorted(zip(nums, list(range(len(nums)))))
        lookup = {i:new_i for new_i, (_, i) in enumerate(sorted_nums)}

        # Count the smaller elements after the number.
        result, bit = [0]*len(nums), BIT(len(nums))
        for i in reversed(range(len(nums))):
            result[i] = bit.query(lookup[i]-1)
            bit.add(lookup[i], 1)
        return result


