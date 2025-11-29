class Solution:
    def minimumDistance(self, word):
        NONE = 26
        INF = 10**9
        def get_pos(ch):
            return ord(ch) - 65
        def get_dist(x, y):
            if x == NONE or y == NONE:
                return 0
            rx, cx = divmod(x, 6)
            ry, cy = divmod(y, 6)
            return abs(rx - ry) + abs(cx - cy)
        prev = [[INF] * 27 for _ in range(27)]
        prev[NONE][NONE] = 0
        for ch in word:
            target = get_pos(ch)
            curr = [[INF] * 27 for _ in range(27)]
            for left in range(27):
                for right in range(27):
                    if prev[left][right] == INF:
                        continue
                    cost_left = prev[left][right] + get_dist(left, target)
                    curr[target][right] = min(curr[target][right], cost_left)
                    cost_right = prev[left][right] + get_dist(right, target)
                    curr[left][target] = min(curr[left][target], cost_right)
            prev = curr
        return min(min(r) for r in prev)
