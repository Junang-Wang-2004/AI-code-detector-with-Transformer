# Time:  O(nlogn)
# Space: O(n)
import bisect


# prefix sum, binary search
class Solution4(object):
    def maximumWhiteTiles(self, tiles, carpetLen):
        """
        """
        tiles.sort()
        prefix = [0]*(len(tiles)+1)
        for i, (l, r) in enumerate(tiles):
            prefix[i+1] = prefix[i]+(r-l+1)
        result = 0
        for right, (_, r) in enumerate(tiles):
            l = r-carpetLen+1
            left = bisect.bisect_right(tiles, [l])
            if left-1 >= 0 and tiles[left-1][1]+1 >= l:
                left -= 1
            extra = max(l-tiles[left][0], 0)
            result = max(result, (prefix[right+1]-prefix[left])-extra)
        return result
