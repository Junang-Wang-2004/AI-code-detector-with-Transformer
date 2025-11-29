class C1(object):

    def isPossible(self, a1, a2):
        """
        """
        v1 = [set() for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3 - 1].add(v4 - 1)
            v1[v4 - 1].add(v3 - 1)
        v5 = [v3 for v3 in range(a1) if len(v1[v3]) % 2]
        if len(v5) == 0:
            return True
        if len(v5) == 2:
            return any((v5[0] not in v1[v3] and v5[1] not in v1[v3] for v3 in range(a1)))
        if len(v5) == 4:
            return v5[0] not in v1[v5[1]] and v5[2] not in v1[v5[3]] or (v5[0] not in v1[v5[2]] and v5[1] not in v1[v5[3]]) or (v5[0] not in v1[v5[3]] and v5[1] not in v1[v5[2]])
        return False
