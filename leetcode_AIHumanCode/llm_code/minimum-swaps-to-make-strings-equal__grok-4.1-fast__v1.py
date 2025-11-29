class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        count_xy = 0
        count_yx = 0
        for a, b in zip(s1, s2):
            if a == 'x' and b == 'y':
                count_xy += 1
            elif a == 'y' and b == 'x':
                count_yx += 1
        if count_xy % 2 != count_yx % 2:
            return -1
        total_mismatch = count_xy + count_yx
        return total_mismatch // 2 + count_xy % 2
