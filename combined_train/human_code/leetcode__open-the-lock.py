class C1(object):

    def openLock(self, a1, a2):
        """
        """
        v1 = set(a1)
        v2 = ['0000']
        v3 = {'0000'}
        v4 = 0
        while v2:
            v5 = []
            for v6 in v2:
                if v6 == a2:
                    return v4
                if v6 in v1:
                    continue
                for v7 in range(4):
                    v8 = int(v6[v7])
                    for v9 in (-1, 1):
                        v10 = (v8 + v9) % 10
                        v11 = v6[:v7] + str(v10) + v6[v7 + 1:]
                        if v11 not in v3:
                            v3.add(v11)
                            v5.append(v11)
            v2 = v5
            v4 += 1
        return -1
