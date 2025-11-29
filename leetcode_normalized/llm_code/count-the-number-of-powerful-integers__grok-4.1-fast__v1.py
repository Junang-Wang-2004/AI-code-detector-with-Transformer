class C1(object):

    def numberOfPowerfulInt(self, a1, a2, a3, a4):

        def count_valid(a1):
            if a1 < 0:
                return 0
            v1 = str(a1)
            v2 = len(a4)
            v3 = v1[:-v2]
            v4 = v1[-v2:]
            v5 = int(a4)
            v6 = int(v4)
            v7 = len(v3)
            v8 = 0
            v9 = a3 + 1
            v10 = pow(v9, v7)
            for v11 in range(v7):
                v10 //= v9
                v12 = int(v3[v11])
                v13 = min(v12 - 1, a3) + 1
                v8 += v13 * v10
                if v12 > a3:
                    break
            else:
                if v6 >= v5:
                    v8 += 1
            return v8
        return count_valid(a2) - count_valid(a1 - 1)
