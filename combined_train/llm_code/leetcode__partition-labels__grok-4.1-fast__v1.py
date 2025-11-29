class C1:

    def partitionLabels(self, a1):
        v1 = len(a1)
        v2 = [-1] * 26
        v3 = v1 - 1
        while v3 >= 0:
            v4 = ord(a1[v3]) - ord('a')
            if v2[v4] == -1:
                v2[v4] = v3
            v3 -= 1
        v5 = []
        v6 = 0
        v7 = 0
        v3 = 0
        while v3 < v1:
            v7 = max(v7, v2[ord(a1[v3]) - ord('a')])
            if v3 == v7:
                v5.append(v3 - v6 + 1)
                v6 = v3 + 1
            v3 += 1
        return v5
