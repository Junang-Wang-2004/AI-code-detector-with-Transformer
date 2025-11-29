# Time:  O(nlogn)
# Space: O(1)

# sliding window, optimized from solution3
class Solution(object):
    def maximumWhiteTiles(self, tiles, carpetLen):
        """
        """
        tiles.sort()
        result = right = gap = 0
        for left, (l, _) in enumerate(tiles):
            if left-1 >= 0:
                gap -= tiles[left][0]-tiles[left-1][1]-1
            r = l+carpetLen-1
            while right+1 < len(tiles) and r+1 >= tiles[right+1][0]:
                right += 1
                gap += tiles[right][0]-tiles[right-1][1]-1
            result = max(result, min(tiles[right][1]-tiles[left][0]+1, carpetLen)-gap)
        return result


