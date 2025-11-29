class C1:

    def shortestBeautifulSubstring(self, a1, a2):
        v1 = len(a1)
        v2 = float('inf')
        v3 = ''
        for v4 in range(v1):
            if a1[v4] != '1':
                continue
            v5 = 1
            v6 = v4
            while v6 < v1 and v5 < a2:
                v6 += 1
                if a1[v6] == '1':
                    v5 += 1
            if v5 == a2:
                v7 = a1[v4:v6 + 1]
                v8 = len(v7)
                if v8 < v2:
                    v2 = v8
                    v3 = v7
                elif v8 == v2 and v7 < v3:
                    v3 = v7
        return v3
