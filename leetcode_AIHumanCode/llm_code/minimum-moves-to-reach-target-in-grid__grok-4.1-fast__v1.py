class Solution(object):
    def minMoves(self, sx, sy, tx, ty):
        x0, y0 = sx, sy
        x, y = tx, ty
        ans = 0
        while x != x0 or y != y0:
            if x < x0 or y < y0:
                return -1
            if x == y:
                if x0 == 0:
                    x = 0
                elif y0 == 0:
                    y = 0
                else:
                    return -1
            elif x < y:
                half = y // 2
                if x > half:
                    y -= x
                else:
                    if y % 2:
                        return -1
                    y = half
            else:
                half = x // 2
                if y > half:
                    x -= y
                else:
                    if x % 2:
                        return -1
                    x = half
            ans += 1
        return ans
