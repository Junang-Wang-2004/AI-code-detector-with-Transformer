class C1(object):

    def partitionString(self, a1):
        v1 = [[-1] * 26]
        v2 = 0
        v3 = []
        v4 = []

        def alloc():
            v1.append([-1] * 26)
            return len(v1) - 1
        for v5 in a1:
            v4.append(v5)
            v6 = ord(v5) - ord('a')
            if v1[v2][v6] == -1:
                v1[v2][v6] = alloc()
                v2 = 0
            else:
                v2 = v1[v2][v6]
            if v2:
                continue
            v3.append(''.join(v4))
            v4 = []
        if v4:
            v3.append(''.join(v4))
        return v3
