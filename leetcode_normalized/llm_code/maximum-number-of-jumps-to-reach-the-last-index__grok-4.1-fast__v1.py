class C1(object):

    def maximumJumps(self, a1, a2):
        v1 = len(a1)
        v2 = [float('-inf')] * v1
        v2[0] = 0
        for v3 in range(v1):
            if v2[v3] == float('-inf'):
                continue
            for v4 in range(v3 + 1, v1):
                if abs(a1[v4] - a1[v3]) <= a2:
                    v2[v4] = max(v2[v4], v2[v3] + 1)
        v5 = v2[-1]
        return v5 if v5 != float('-inf') else -1
