# Time:  O(nlogn)
# Space: O(n)
import bisect


# prefix sum, binary search
class Solution3(object):
    def maximumWhiteTiles(self, tiles, carpetLen):
        """
        """
        tiles.sort()
        prefix = [0]*(len(tiles)+1)
        for i, (l, r) in enumerate(tiles):
            prefix[i+1] = prefix[i]+(r-l+1)
        result = 0
        for left, (l, _) in enumerate(tiles):
            r = l+carpetLen-1
            right = bisect.bisect_right(tiles, [r+1])-1
            extra = max(tiles[right][1]-r, 0)
            result = max(result, (prefix[right+1]-prefix[left])-extra)
        return result


