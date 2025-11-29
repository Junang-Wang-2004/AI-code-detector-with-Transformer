class C1(object):

    def findReplaceString(self, a1, a2, a3, a4):
        v1 = {}
        for v2, v3, v4 in zip(a2, a3, a4):
            if a1[v2:v2 + len(v3)] == v3:
                v1[v2] = (len(v3), v4)
        v5 = []
        v2 = 0
        while v2 < len(a1):
            if v2 in v1:
                v6, v7 = v1[v2]
                v5.append(v7)
                v2 += v6
            else:
                v5.append(a1[v2])
                v2 += 1
        return ''.join(v5)
