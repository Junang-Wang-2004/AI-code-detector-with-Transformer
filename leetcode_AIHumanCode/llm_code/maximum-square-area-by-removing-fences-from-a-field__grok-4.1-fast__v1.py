class Solution(object):
    def maximizeSquareArea(self, m, n, hFences, vFences):
        MOD = 10**9 + 7
        def possible_sides(fences, max_pos):
            pos = sorted(set(fences + [1, max_pos]))
            sides = set()
            for i in range(len(pos)):
                for j in range(i + 1, len(pos)):
                    sides.add(pos[j] - pos[i])
            return sides
        horiz_sides = possible_sides(hFences, m)
        vert_sides = possible_sides(vFences, n)
        max_s = max((s for s in horiz_sides if s in vert_sides), default=-1)
        return (max_s * max_s % MOD) if max_s != -1 else -1
