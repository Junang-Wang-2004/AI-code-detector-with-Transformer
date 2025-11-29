class C1(object):

    def minZeroArray(self, a1, a2):
        """
        """

        def binary_search(a1, a2, a3):
            while a1 <= a2:
                v1 = a1 + (a2 - a1) // 2
                if a3(v1):
                    a2 = v1 - 1
                else:
                    a1 = v1 + 1
            return a1

        def check(a1):
            v1 = [0] * (len(a1) + 1)
            for v2 in range(a1):
                v1[a2[v2][0]] += a2[v2][2]
                v1[a2[v2][1] + 1] -= a2[v2][2]
            v3 = 0
            for v2 in range(len(a1)):
                v3 += v1[v2]
                if a1[v2] > v3:
                    return False
            return True
        v1 = binary_search(0, len(a2), check)
        return v1 if v1 <= len(a2) else -1
