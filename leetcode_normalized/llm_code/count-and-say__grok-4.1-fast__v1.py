class C1:

    def countAndSay(self, a1):
        v1 = '1'
        for v2 in range(a1 - 1):
            v3 = []
            v4 = 0
            v5 = len(v1)
            while v4 < v5:
                v6 = v1[v4]
                v7 = 1
                v4 += 1
                while v4 < v5 and v1[v4] == v6:
                    v7 += 1
                    v4 += 1
                v3.append(str(v7) + v6)
            v1 = ''.join(v3)
        return v1
