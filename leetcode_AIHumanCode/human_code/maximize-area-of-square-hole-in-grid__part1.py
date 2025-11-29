# Time:  O(h + v), h = len(hBars), v = len(vBars)
# Space: O(h + v)

# array, hash table
class Solution(object):
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        """
        """
        def max_gap(arr):
            result = l = 1
            lookup = set(arr)
            while lookup:
                x = next(iter(lookup))
                left = x
                while left-1 in lookup:
                    left -= 1
                right = x
                while right+1 in lookup:
                    right += 1
                for i in range(left, right+1):
                    lookup.remove(i)
                result = max(result, (right-left+1)+1)
            return result

        return min(max_gap(hBars), max_gap(vBars))**2


