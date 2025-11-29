from collections import defaultdict

class C1:

    def possibleBipartition(self, a1, a2):
        v1 = defaultdict(list)
        for v2, v3 in a2:
            v1[v2 - 1].append(v3 - 1)
            v1[v3 - 1].append(v2 - 1)
        v4 = [0] * a1

        def explore(a1, a2):
            v4[a1] = a2
            for v1 in v1[a1]:
                if v4[v1] == 0:
                    if not explore(v1, 3 - a2):
                        return False
                elif v4[v1] == a2:
                    return False
            return True
        for v5 in range(a1):
            if v4[v5] == 0:
                if not explore(v5, 1):
                    return False
        return True
