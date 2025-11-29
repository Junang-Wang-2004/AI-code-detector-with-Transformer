from functools import cache

class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        @cache
        def dfs(i: int, j: int, d: int) -> bool:
            n1, n2 = len(s1), len(s2)
            if i == n1 and j == n2:
                return d == 0
            if i < n1 and s1[i].isdigit():
                ni = i
                while ni < n1 and s1[ni].isdigit():
                    ni += 1
                for val in possible(s1[i:ni]):
                    if dfs(ni, j, d + val):
                        return True
                return False
            if j < n2 and s2[j].isdigit():
                nj = j
                while nj < n2 and s2[nj].isdigit():
                    nj += 1
                for val in possible(s2[j:nj]):
                    if dfs(i, nj, d - val):
                        return True
                return False
            if d < 0:
                return dfs(i + 1, j, d + 1) if i < n1 else False
            if d > 0:
                return dfs(i, j + 1, d - 1) if j < n2 else False
            return i < n1 and j < n2 and s1[i] == s2[j] and dfs(i + 1, j + 1, d)

        def possible(seq: str) -> set[int]:
            vals = set()
            def rec(pos: int, sumv: int):
                if pos == len(seq):
                    vals.add(sumv)
                    return
                num = 0
                for end in range(pos, len(seq)):
                    num = num * 10 + int(seq[end])
                    rec(end + 1, sumv + num)
            rec(0, 0)
            return vals

        return dfs(0, 0, 0)
