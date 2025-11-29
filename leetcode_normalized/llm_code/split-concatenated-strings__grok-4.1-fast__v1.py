class C1(object):

    def splitLoopedString(self, a1):
        v1 = [max(s, s[::-1]) for v2 in a1]
        v3 = ''.join(v1)
        v4 = len(v3)
        v5 = 'a'
        v6 = [0]
        for v2 in a1:
            v6.append(v6[-1] + len(v2))
        v7 = len(a1)
        for v8 in range(v7):
            v9 = v6[v8]
            v10 = v6[v8 + 1]
            v11 = v3[v10:] + v3[:v9]
            v12 = v10 - v9
            v13 = a1[v8]
            for v14 in (v13, v13[::-1]):
                for v15 in range(v12):
                    if v14[v15] >= v5[0]:
                        v16 = v14[v15:] + v11 + v14[:v15]
                        v5 = max(v5, v16)
        return v5
