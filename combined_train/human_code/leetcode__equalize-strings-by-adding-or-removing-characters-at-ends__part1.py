class C1(object):

    def minOperations(self, a1, a2):
        """
        """

        def binary_search_right(a1, a2, a3):
            while a1 <= a2:
                v1 = a1 + (a2 - a1) // 2
                if not a3(v1):
                    a2 = v1 - 1
                else:
                    a1 = v1 + 1
            return a2

        def rolling_hash(a1, a2, a3, a4):
            v1, v2 = (10 ** 9 + 7, 113)
            v3 = 0
            v4 = pow(v2, a2 - 1, v1)
            for v5 in range(len(a1)):
                v3 = (v3 * v2 + (ord(a1[v5]) - ord('a'))) % v1
                if v5 < a2 - 1:
                    continue
                if not a4:
                    a3.add(v3)
                elif v3 in a3:
                    return True
                v3 = (v3 - (ord(a1[v5 - (a2 - 1)]) - ord('a')) * v4) % v1
            return False

        def check(a1):
            v1 = set()
            rolling_hash(a2, a1, v1, False)
            return rolling_hash(a1, a1, v1, True)
        if len(a1) < len(a2):
            a1, a2 = (a2, a1)
        return len(a1) + len(a2) - 2 * binary_search_right(1, min(len(a1), min(a2)), check)
