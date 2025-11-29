from functools import cache

class C1:

    def possiblyEquals(self, a1: str, a2: str) -> bool:

        @cache
        def dfs(a1: int, a2: int, a3: int) -> bool:
            v1, v2 = (len(a1), len(a2))
            if a1 == v1 and a2 == v2:
                return a3 == 0
            if a1 < v1 and a1[a1].isdigit():
                v3 = a1
                while v3 < v1 and a1[v3].isdigit():
                    v3 += 1
                for v4 in possible(a1[a1:v3]):
                    if dfs(v3, a2, a3 + v4):
                        return True
                return False
            if a2 < v2 and a2[a2].isdigit():
                v5 = a2
                while v5 < v2 and a2[v5].isdigit():
                    v5 += 1
                for v4 in possible(a2[a2:v5]):
                    if dfs(a1, v5, a3 - v4):
                        return True
                return False
            if a3 < 0:
                return dfs(a1 + 1, a2, a3 + 1) if a1 < v1 else False
            if a3 > 0:
                return dfs(a1, a2 + 1, a3 - 1) if a2 < v2 else False
            return a1 < v1 and a2 < v2 and (a1[a1] == a2[a2]) and dfs(a1 + 1, a2 + 1, a3)

        def possible(a1: str) -> set[int]:
            v1 = set()

            def rec(a1: int, a2: int):
                if a1 == len(a1):
                    v1.add(a2)
                    return
                v1 = 0
                for v2 in range(a1, len(a1)):
                    v1 = v1 * 10 + int(a1[v2])
                    rec(v2 + 1, a2 + v1)
            rec(0, 0)
            return v1
        return dfs(0, 0, 0)
