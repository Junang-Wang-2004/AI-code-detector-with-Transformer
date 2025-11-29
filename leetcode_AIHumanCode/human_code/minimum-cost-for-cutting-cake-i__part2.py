# Time:  O(mlogm + nlogn)
# Space: O(1)
# sort, greedy
class Solution2(object):
    def minimumCost(self, m, n, horizontalCut, verticalCut):
        """
        """
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)
        result = i = j = 0
        while i < len(horizontalCut) or j < len(verticalCut):
            if j == len(verticalCut) or (i < len(horizontalCut) and horizontalCut[i] > verticalCut[j]):
                result += horizontalCut[i]*(j+1)
                i += 1
            else:
                result += verticalCut[j]*(i+1)
                j += 1
        return result


