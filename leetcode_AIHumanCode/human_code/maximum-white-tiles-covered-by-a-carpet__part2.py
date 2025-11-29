# Time:  O(nlogn)
# Space: O(1)
# sliding window, optimized from solution4
class Solution2(object):
    def maximumWhiteTiles(self, tiles, carpetLen):
        """
        """
        tiles.sort()
        result = left = gap = 0
        for right in range(len(tiles)):
            if right-1 >= 0:
                gap += tiles[right][0]-tiles[right-1][1]-1
            l = tiles[right][1]-carpetLen+1
            while not (tiles[left][1]+1 >= l):
                left += 1
                gap -= tiles[left][0]-tiles[left-1][1]-1
            result = max(result, min(tiles[right][1]-tiles[left][0]+1, carpetLen)-gap)
        return result


