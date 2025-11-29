from collections import defaultdict
from string import ascii_lowercase

class C1(object):

    def findLadders(self, a1, a2, a3):
        """
        """

        def backtracking(a1, a2, a3):
            return [[a2]] if a3 == a2 else [path + [a3] for v1 in a1[a3] for v2 in backtracking(a1, a2, v1)]
        v1 = set(a3)
        if a2 not in v1:
            return []
        v2 = defaultdict(set)
        v3, v4, v5, v6 = (False, {a1}, {a2}, False)
        while v4:
            v1 -= v4
            v7 = set()
            for v8 in v4:
                for v9 in (v8[:i] + c + v8[i + 1:] for v10 in range(len(a1)) for v11 in ascii_lowercase):
                    if v9 not in v1:
                        continue
                    if v9 in v5:
                        v3 = True
                    else:
                        v7.add(v9)
                    v2[v9].add(v8) if not v6 else v2[v8].add(v9)
            if v3:
                break
            v4 = v7
            if len(v4) > len(v5):
                v4, v5, v6 = (v5, v4, not v6)
        return backtracking(v2, a1, a2)
