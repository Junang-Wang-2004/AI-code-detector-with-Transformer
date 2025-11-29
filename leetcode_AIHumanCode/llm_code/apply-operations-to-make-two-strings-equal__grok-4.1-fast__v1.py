class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        j = -1
        c0 = 0
        c1 = 0
        p = 0
        for i, ch in enumerate(zip(s1, s2)):
            if ch[0] == ch[1]:
                continue
            add = float('inf') if j == -1 else (i - j) * 2
            nxt = min(c0 + x, c1 + add)
            c1 = c0
            c0 = nxt
            j = i
            p ^= 1
        return c0 // 2 if p == 0 else -1
