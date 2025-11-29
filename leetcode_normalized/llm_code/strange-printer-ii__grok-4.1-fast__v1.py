from collections import defaultdict

class C1:

    def isPrintable(self, a1):
        if not a1 or not a1[0]:
            return True
        v1, v2 = (len(a1), len(a1[0]))
        v3 = {}
        for v4 in range(v1):
            for v5 in range(v2):
                v6 = a1[v4][v5]
                if v6 not in v3:
                    v3[v6] = [v4, v5, v4, v5]
                else:
                    v7 = v3[v6]
                    v7[0] = min(v7[0], v4)
                    v7[1] = min(v7[1], v5)
                    v7[2] = max(v7[2], v4)
                    v7[3] = max(v7[3], v5)
        v8 = defaultdict(set)
        for v6, (v9, v10, v11, v12) in v3.items():
            for v13 in range(v9, v11 + 1):
                for v14 in range(v10, v12 + 1):
                    v15 = a1[v13][v14]
                    if v15 != v6:
                        v8[v6].add(v15)
        v16 = {}

        def detect_cycle(a1):
            if a1 in v16:
                return v16[a1] == 1
            v16[a1] = 1
            for v1 in v8[a1]:
                if detect_cycle(v1):
                    return True
            v16[a1] = 2
            return False
        for v6 in v3:
            if v6 not in v16:
                if detect_cycle(v6):
                    return False
        return True
