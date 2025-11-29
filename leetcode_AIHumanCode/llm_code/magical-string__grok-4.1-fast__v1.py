class Solution:
    def magicalString(self, n):
        s = [1, 2, 2]
        idx = 0
        val = 1
        while len(s) < n:
            for _ in range(s[idx]):
                if len(s) < n:
                    s.append(val)
            idx += 1
            val = 3 - val
        return sum(v == 1 for v in s)
