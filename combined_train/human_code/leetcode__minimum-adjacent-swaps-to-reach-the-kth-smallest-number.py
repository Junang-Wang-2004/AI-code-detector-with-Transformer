class C1(object):

    def getMinSwaps(self, a1, a2):
        """
        """

        def next_permutation(a1, a2, a3):

            def reverse(a1, a2, a3):
                v1, v2 = (a2, a3 - 1)
                while v1 < v2:
                    a1[v1], a1[v2] = (a1[v2], a1[v1])
                    v1 += 1
                    v2 -= 1
            v1, v2 = (a2 - 1, a2)
            for v3 in reversed(range(a2, a3 - 1)):
                if a1[v3] < a1[v3 + 1]:
                    v1 = v3
                    break
            else:
                reverse(a1, a2, a3)
                return False
            for v3 in reversed(range(v1 + 1, a3)):
                if a1[v3] > a1[v1]:
                    v2 = v3
                    break
            a1[v1], a1[v2] = (a1[v2], a1[v1])
            reverse(a1, v1 + 1, a3)
            return True
        v1 = list(a1)
        while a2:
            next_permutation(v1, 0, len(v1))
            a2 -= 1
        v3 = 0
        for v4 in range(len(v1)):
            if v1[v4] == a1[v4]:
                continue
            for v5 in range(v4 + 1, len(v1)):
                if v1[v5] == a1[v4]:
                    break
            v3 += v5 - v4
            for v5 in reversed(range(v4 + 1, v5 + 1)):
                v1[v5], v1[v5 - 1] = (v1[v5 - 1], v1[v5])
        return v3
