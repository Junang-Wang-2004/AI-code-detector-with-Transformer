class C1(object):

    def maximumNumber(self, a1, a2):
        v1 = len(a1)
        v2 = -1
        for v3 in range(v1):
            v4 = int(a1[v3])
            if a2[v4] > v4:
                v2 = v3
                break
        if v2 == -1:
            return a1
        v5 = v1
        for v3 in range(v2, v1):
            v4 = int(a1[v3])
            if a2[v4] < v4:
                v5 = v3
                break
        v6 = []
        for v3 in range(v1):
            v4 = int(a1[v3])
            if v2 <= v3 < v5:
                v6.append(str(a2[v4]))
            else:
                v6.append(a1[v3])
        return ''.join(v6)
