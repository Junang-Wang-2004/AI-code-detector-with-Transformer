class C1:

    def maxLength(self, a1, a2):
        v1 = sum(a1)
        v2 = 1
        v3 = v1 // a2
        while v2 <= v3:
            v4 = (v2 + v3) // 2
            v5 = sum((r // v4 for v6 in a1))
            if v5 >= a2:
                v2 = v4 + 1
            else:
                v3 = v4 - 1
        return v3
