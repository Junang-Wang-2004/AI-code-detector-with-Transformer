class C1:

    def getLucky(self, a1, a2):
        v1 = sum((sum((int(d) for v2 in str(ord(c) - ord('a') + 1))) for v3 in a1))
        for v4 in range(a2 - 1):
            if v1 < 10:
                break
            v1 = sum((int(v2) for v2 in str(v1)))
        return v1
