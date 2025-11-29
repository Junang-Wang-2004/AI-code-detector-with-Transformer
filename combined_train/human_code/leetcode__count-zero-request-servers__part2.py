class C1(object):

    def countServers(self, a1, a2, a3, a4):
        """
        """
        v1 = []
        for v2, v3 in a2:
            v1.append((v3, +1, v2 - 1))
            v1.append((v3 + a3 + 1, -1, v2 - 1))
        v1.append((float('inf'), 0, 0))
        v1.sort()
        v4 = []
        for v5, v3 in enumerate(a4):
            v4.append((v3, v5))
        v4.sort(reverse=True)
        v6 = [0] * len(a4)
        v7 = [0] * a1
        v8 = 0
        for v3, v9, v5 in v1:
            while v4 and v4[-1][0] < v3:
                v6[v4.pop()[1]] += a1 - v8
            if v7[v5] == 0:
                v8 += 1
            v7[v5] += v9
            if v7[v5] == 0:
                v8 -= 1
        return v6
