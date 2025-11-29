class C1:

    def pushDominoes(self, a1):
        v1 = len(a1)
        v2 = [v1] * v1
        v3 = [v1] * v1
        v4 = -1
        for v5 in range(v1):
            if a1[v5] == 'R':
                v4 = v5
            elif a1[v5] == 'L':
                v4 = -1
            elif v4 != -1:
                v2[v5] = v5 - v4
        v6 = v1
        for v5 in range(v1 - 1, -1, -1):
            if a1[v5] == 'L':
                v6 = v5
            elif a1[v5] == 'R':
                v6 = v1
            elif v6 != v1:
                v3[v5] = v6 - v5
        v7 = []
        for v5 in range(v1):
            if a1[v5] != '.':
                v7.append(a1[v5])
            else:
                v8 = v2[v5]
                v9 = v3[v5]
                if v8 < v9:
                    v7.append('R')
                elif v8 > v9:
                    v7.append('L')
                else:
                    v7.append('.')
        return ''.join(v7)
