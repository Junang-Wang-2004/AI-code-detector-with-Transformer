class Solution(object):
    def numberOfCleanRooms(self, room):
        rows = len(room)
        if rows == 0:
            return 0
        cols = len(room[0])
        dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        ans = i = j = dir_id = 0
        while True:
            bit_pos = 1 << (dir_id + 1)
            if room[i][j] & bit_pos:
                return ans
            if (room[i][j] & ~1) == 0:
                ans += 1
            room[i][j] |= bit_pos
            di, dj = dirs[dir_id]
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < cols and room[ni][nj] % 2 == 0:
                i, j = ni, nj
            else:
                dir_id = (dir_id + 1) % 4
