class C1(object):

    def recoverArray(self, a1, a2):
        """
        """
        a2.sort()
        v1, v2 = (0, len(a2))
        v3 = []
        for v4 in range(a1):
            v5 = a2[0] - a2[1]
            assert v5 <= 0
            v6, v7, v8 = (False, 0, 0)
            for v9 in range(v2):
                if v8 < v7 and a2[v8] == a2[v9]:
                    v8 += 1
                else:
                    if v1 == a2[v9] - v5:
                        v6 = True
                    a2[v7] = a2[v9] - v5
                    v7 += 1
            if v6:
                v3.append(v5)
            else:
                v3.append(-v5)
                v1 -= v5
            v2 //= 2
        return v3
