# Time:  O(n)
# Space: O(1)
class Solution2(object):
    def maxAbsValExpr(self, arr1, arr2):
        """
        """
        return max(max(c1*arr1[i] + c2*arr2[i] + i for i in range(len(arr1))) -
                   min(c1*arr1[i] + c2*arr2[i] + i for i in range(len(arr1)))
                   for c1 in [1, -1] for c2 in [1, -1])
