class C1:

    def modifyString(self, a1):
        v1 = list(a1)
        v2 = len(v1)
        for v3 in range(v2):
            if v1[v3] == '?':
                v4 = set()
                if v3 > 0:
                    v4.add(v1[v3 - 1])
                if v3 < v2 - 1:
                    v4.add(v1[v3 + 1])
                for v5 in 'abc':
                    if v5 not in v4:
                        v1[v3] = v5
                        break
        return ''.join(v1)
