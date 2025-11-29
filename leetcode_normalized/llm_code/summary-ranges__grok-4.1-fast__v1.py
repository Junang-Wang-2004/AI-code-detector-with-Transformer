class C1:

    def summaryRanges(self, a1):
        v1 = []
        v2 = 0
        v3 = len(a1)
        while v2 < v3:
            v4 = v2
            while v4 + 1 < v3 and a1[v4 + 1] == a1[v4] + 1:
                v4 += 1
            if v2 == v4:
                v1.append(f'{a1[v2]}')
            else:
                v1.append(f'{a1[v2]}->{a1[v4]}')
            v2 = v4 + 1
        return v1
