class C1(object):

    def closestMeetingNode(self, a1, a2, a3):
        v1 = len(a1)
        v2 = [-1] * v1
        v3 = a2
        v4 = 0
        while v3 != -1 and v2[v3] == -1:
            v2[v3] = v4
            v4 += 1
            v3 = a1[v3]
        v5 = [-1] * v1
        v3 = a3
        v4 = 0
        while v3 != -1 and v5[v3] == -1:
            v5[v3] = v4
            v4 += 1
            v3 = a1[v3]
        v6 = -1
        v7 = float('inf')
        for v8 in range(v1):
            if v2[v8] != -1 and v5[v8] != -1:
                v9 = max(v2[v8], v5[v8])
                if v9 < v7 or (v9 == v7 and v8 < v6):
                    v7 = v9
                    v6 = v8
        return v6
