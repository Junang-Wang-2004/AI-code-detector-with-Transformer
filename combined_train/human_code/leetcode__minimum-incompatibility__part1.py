import itertools

class C1(object):

    def minimumIncompatibility(self, a1, a2):
        """
        """
        v1 = (len(a1) - 1) * (len(a1) // a2) + 1

        def backtracking(a1, a2, a3):
            if not a1:
                return 0
            if a1 not in a3:
                v1 = v1
                for v2 in itertools.combinations(a1, a2):
                    v3 = set(v2)
                    if len(v3) < a2:
                        continue
                    v4 = []
                    for v5 in a1:
                        if v5 in v3:
                            v3.remove(v5)
                            continue
                        v4.append(v5)
                    v1 = min(v1, max(v2) - min(v2) + backtracking(tuple(v4), a2, a3))
                a3[a1] = v1
            return a3[a1]
        v2 = backtracking(tuple(a1), len(a1) // a2, {})
        return v2 if v2 != v1 else -1
