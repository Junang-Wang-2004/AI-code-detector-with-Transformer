class C1:

    def isCovered(self, a1, a2, a3):
        a1.sort(key=lambda x: x[0])
        v1 = 0
        v2 = a2
        while v2 <= a3:
            v3 = v2 - 1
            while v1 < len(a1) and a1[v1][0] <= v2:
                v3 = max(v3, a1[v1][1])
                v1 += 1
            if v3 < v2:
                return False
            v2 = v3 + 1
        return True
