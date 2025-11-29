class C1(object):

    def countMentions(self, a1, a2):
        v1 = a1
        v2 = [0] * v1
        v3 = [1] * v1
        v4 = sorted(a2, key=lambda x: (int(x[1]), 0 if x[0] == 'OFFLINE' else 1))
        for v5, v6, v7 in v4:
            v8 = int(v6)
            if v5 == 'OFFLINE':
                v3[int(v7)] = v8 + 60
            elif v7 == 'ALL':
                for v9 in range(v1):
                    v2[v9] += 1
            elif v7 == 'HERE':
                for v9 in range(v1):
                    if v3[v9] <= v8:
                        v2[v9] += 1
            else:
                for v10 in v7.split():
                    v11 = int(v10[2:])
                    v2[v11] += 1
        return v2
