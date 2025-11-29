# Time:  O(hlogh + vlogv), h = len(hBars), v = len(vBars)
# Space: O(1)
# array, sort
class Solution2(object):
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        """
        """
        def max_gap(arr):
            arr.sort()
            result = l = 1
            for i in range(len(arr)):
                l += 1
                result = max(result, l)
                if i+1 != len(arr) and arr[i+1] != arr[i]+1:
                    l = 1
            return result

        return min(max_gap(hBars), max_gap(vBars))**2
