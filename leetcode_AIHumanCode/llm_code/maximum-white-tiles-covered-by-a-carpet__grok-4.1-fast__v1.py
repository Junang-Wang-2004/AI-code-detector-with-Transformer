class Solution:
    def maximumWhiteTiles(self, tiles, carpetLen):
        tiles.sort(key=lambda t: t[0])
        n = len(tiles)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + (tiles[i][1] - tiles[i][0] + 1)
        ans = 0
        j = -1
        for i in range(n):
            target = tiles[i][0] + carpetLen - 1
            while j + 1 < n and tiles[j + 1][0] <= target:
                j += 1
            if j >= i:
                overhang = max(tiles[j][1] - target, 0)
                covered = prefix[j + 1] - prefix[i] - overhang
                if covered > ans:
                    ans = covered
        return ans
