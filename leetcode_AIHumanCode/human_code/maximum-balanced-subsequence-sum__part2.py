# Time:  O(nlogn)
# Space: O(n)
# bit, fenwick tree
class Solution2(object):
    def maxBalancedSubsequenceSum(self, nums):
        """
        """
        NEG_INF = float("-inf")
        class BIT(object):  # 0-indexed.
            def __init__(self, n, default=0, fn=lambda x, y: x+y):
                self.__bit = [NEG_INF]*(n+1)  # Extra one for dummy node.
                self.__default = default
                self.__fn = fn

            def update(self, i, val):
                i += 1  # Extra one for dummy node.
                while i < len(self.__bit):
                    self.__bit[i] = self.__fn(self.__bit[i], val)
                    i += (i & -i)

            def query(self, i):
                i += 1  # Extra one for dummy node.
                ret = self.__default
                while i > 0:
                    ret = self.__fn(ret, self.__bit[i])
                    i -= (i & -i)
                return ret

        val_to_idx = {x:i for i, x in enumerate(sorted({x-i for i, x in enumerate(nums)}))}
        bit = BIT(len(val_to_idx), default=NEG_INF, fn=max)
        for i, x in enumerate(nums):
            v = max(bit.query(val_to_idx[x-i]), 0)+x
            bit.update(val_to_idx[x-i], v)
        return bit.query(len(val_to_idx)-1)


