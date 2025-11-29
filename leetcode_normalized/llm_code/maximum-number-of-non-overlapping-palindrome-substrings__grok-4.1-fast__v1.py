class C1:

    def maxPalindromes(self, a1, a2):

        def find_next_start(a1, a2):
            v1, v2 = divmod(a1, 2)
            while v1 >= a2 and v2 < len(a1) and (a1[v1] == a1[v2]):
                if v2 - v1 + 1 >= a2:
                    return v2 + 1
                v1 -= 1
                v2 += 1
            return -1
        v1 = len(a1)
        v2 = 0
        v3 = 0
        for v4 in range(2 * v1 - 1):
            v5 = find_next_start(v4, v3)
            if v5 != -1:
                v3 = v5
                v2 += 1
        return v2
