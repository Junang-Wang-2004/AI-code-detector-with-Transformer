import collections

class C1:

    def findNumOfValidWords(self, a1, a2):
        v1 = collections.Counter()
        for v2 in a1:
            v3 = 0
            for v4 in v2:
                v3 |= 1 << ord(v4) - ord('a')
            v1[v3] += 1
        v5 = []
        for v6 in a2:
            v7 = 0
            v8 = ord(v6[0]) - ord('a')
            v9 = 1 << v8
            for v4 in v6:
                v7 |= 1 << ord(v4) - ord('a')
            v10 = 0
            v11 = v7
            while v11:
                if v11 & v9:
                    v10 += v1[v11]
                v11 = v11 - 1 & v7
            v5.append(v10)
        return v5
