class C1(object):

    def circularArrayLoop(self, a1):
        v1 = len(a1)
        for v2 in range(v1):
            if a1[v2] == 0:
                continue
            v3 = a1[v2]
            v4 = v2
            v5 = v2
            while True:
                v6 = (v4 + a1[v4]) % v1
                if a1[v6] * v3 <= 0:
                    break
                v7 = (v5 + a1[v5]) % v1
                if a1[v7] * v3 <= 0:
                    break
                v8 = (v7 + a1[v7]) % v1
                if a1[v8] * v3 <= 0:
                    break
                v4 = v6
                v5 = v8
                if v4 == v5:
                    v9 = (v4 + a1[v4]) % v1
                    if v9 != v4:
                        return True
                    break
            v10 = v2
            while a1[v10] * v3 > 0:
                v11 = (v10 + a1[v10]) % v1
                a1[v10] = 0
                v10 = v11
        return False
