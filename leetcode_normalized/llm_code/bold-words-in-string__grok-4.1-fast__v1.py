class C1(object):

    def boldWords(self, a1, a2):
        v1 = []
        v2 = len(a2)
        for v3 in range(v2):
            for v4 in a1:
                v5 = len(v4)
                if v3 + v5 > v2:
                    continue
                if a2[v3:v3 + v5] == v4:
                    v1.append((v3, v3 + v5 - 1))
        if not v1:
            return a2
        v1.sort()
        v6 = [list(v1[0])]
        for v7, v8 in v1[1:]:
            v9, v10 = v6[-1]
            if v10 + 1 >= v7:
                v6[-1][1] = max(v10, v8)
            else:
                v6.append([v7, v8])
        v11 = []
        v12 = 0
        for v13, v14 in v6:
            v11.append(a2[v12:v13])
            v11.append('<b>')
            v11.append(a2[v13:v14 + 1])
            v11.append('</b>')
            v12 = v14 + 1
        v11.append(a2[v12:])
        return ''.join(v11)
