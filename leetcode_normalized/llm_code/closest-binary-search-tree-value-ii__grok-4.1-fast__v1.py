class C1(object):

    def closestKValues(self, a1, a2, a3):
        v1 = []
        v2 = a1
        v3 = []
        while v2 or v3:
            while v2:
                v3.append(v2)
                v2 = v2.left
            v2 = v3.pop()
            v1.append(v2.val)
            v2 = v2.right
        v4 = 0
        while v4 < len(v1) and v1[v4] < a2:
            v4 += 1
        v5 = v4 - 1
        v6 = v4
        v7 = []
        for v8 in range(a3):
            if v5 < 0:
                v7.append(v1[v6])
                v6 += 1
            elif v6 == len(v1):
                v7.append(v1[v5])
                v5 -= 1
            else:
                v9 = abs(v1[v5] - a2)
                v10 = abs(v1[v6] - a2)
                if v9 <= v10:
                    v7.append(v1[v5])
                    v5 -= 1
                else:
                    v7.append(v1[v6])
                    v6 += 1
        return sorted(v7)
