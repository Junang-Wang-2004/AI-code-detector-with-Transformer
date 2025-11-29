class C1:

    def minOperations(self, a1, a2):
        v1 = len(a1)
        v2 = []
        for v3 in range(2):
            v4 = a2[v1 - 1] if v3 else a1[v1 - 1]
            v5 = a1[v1 - 1] if v3 else a2[v1 - 1]
            v6 = 0
            v7 = True
            for v8 in range(v1):
                v9 = a1[v8]
                v10 = a2[v8]
                if v9 <= v4 and v10 <= v5:
                    continue
                if v10 <= v4 and v9 <= v5:
                    v6 += 1
                else:
                    v7 = False
                    break
            if v7:
                v2.append(v6)
        return min(v2) if v2 else -1
