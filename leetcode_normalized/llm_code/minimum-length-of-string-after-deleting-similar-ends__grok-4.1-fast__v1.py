class C1:

    def minimumLength(self, a1):
        v1, v2 = (0, len(a1) - 1)
        while v1 < v2 and a1[v1] == a1[v2]:
            v3 = a1[v2]
            while v1 <= v2 and a1[v2] == v3:
                v2 -= 1
            while v1 <= v2 and a1[v1] == v3:
                v1 += 1
        return max(0, v2 - v1 + 1)
