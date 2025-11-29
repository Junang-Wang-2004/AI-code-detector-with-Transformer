class C1(object):

    def minLength(self, a1, a2):
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

        def lengths():
            v1 = 0
            for v2 in range(len(a1)):
                v1 += 1
                if v2 + 1 == len(a1) or a1[v2 + 1] != a1[v2]:
                    yield v1
                    v1 = 0

        def check(a1):
            if a1 == 1:
                v1 = sum((int(a1) != i % 2 for v2, a1 in enumerate(a1)))
                return min(v1, len(a1) - v1) <= a2
            return sum((l // (a1 + 1) for v3 in lengths())) <= a2
        return binary_search(1, len(a1), check)
