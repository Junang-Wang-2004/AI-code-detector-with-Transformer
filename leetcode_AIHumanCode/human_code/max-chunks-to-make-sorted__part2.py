# Time:  O(n)
# Space: O(n)
# mono stack solution
class Solution2(object):
    def maxChunksToSorted(self, arr):
        """
        """
        result, increasing_stk = 0, []
        for num in arr:
            max_num = num if not increasing_stk else max(increasing_stk[-1], num)
            while increasing_stk and increasing_stk[-1] > num:
                increasing_stk.pop()
            increasing_stk.append(max_num)
        return len(increasing_stk)
