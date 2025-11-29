class C1:

    def grayCode(self, a1):
        v1 = [0]
        for v2 in range(a1):
            v3 = 1 << v2
            v4 = len(v1)
            v5 = v4 - 1
            while v5 >= 0:
                v1.append(v3 | v1[v5])
                v5 -= 1
        return v1
