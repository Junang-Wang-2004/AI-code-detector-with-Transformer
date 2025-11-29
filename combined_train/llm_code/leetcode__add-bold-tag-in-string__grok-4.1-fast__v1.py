class C1:

    def addBoldTag(self, a1, a2):
        v1 = []
        for v2 in a2:
            v3 = len(v2)
            if v3 == 0:
                continue
            v4 = 0
            while True:
                v5 = a1.find(v2, v4)
                if v5 == -1:
                    break
                v1.append((v5, v5 + v3))
                v4 = v5 + 1
        if not v1:
            return a1
        v1.sort()
        v6 = [[v1[0][0], v1[0][1]]]
        for v7, v8 in v1[1:]:
            if v7 <= v6[-1][1]:
                v6[-1][1] = max(v6[-1][1], v8)
            else:
                v6.append([v7, v8])
        v9 = []
        v10 = 0
        for v11, v12 in v6:
            v9.append(a1[v10:v11])
            v9.append('<b>')
            v9.append(a1[v11:v12])
            v9.append('</b>')
            v10 = v12
        v9.append(a1[v10:])
        return ''.join(v9)
