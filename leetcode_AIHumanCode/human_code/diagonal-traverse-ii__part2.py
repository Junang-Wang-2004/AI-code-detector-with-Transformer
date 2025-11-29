# Time:  O(m * n)
# Space: O(m * n)
class Solution2(object):
    def findDiagonalOrder(self, nums):
        """
        """
        result = []
        for r, row in enumerate(nums):
            for c, num in enumerate(row):
                if len(result) <= r+c:
                    result.append([])
                result[r+c].append(num)
        return [num for row in result for num in reversed(row)]
