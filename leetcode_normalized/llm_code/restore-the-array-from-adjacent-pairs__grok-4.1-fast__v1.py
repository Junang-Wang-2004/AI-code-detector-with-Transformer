from collections import defaultdict

class C1:

    def restoreArray(self, a1):
        v1 = defaultdict(list)
        for v2, v3 in a1:
            v1[v2].append(v3)
            v1[v3].append(v2)
        v4 = next((node for v5 in v1 if len(v1[v5]) == 1))
        v6 = [v4]
        v7 = None
        v8 = v4
        v9 = len(a1) + 1
        while len(v6) < v9:
            for v10 in v1[v8]:
                if v10 != v7:
                    v6.append(v10)
                    v7 = v8
                    v8 = v10
                    break
        return v6
