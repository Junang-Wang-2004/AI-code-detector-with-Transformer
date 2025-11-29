class C1(object):

    def minAnagramLength(self, a1):
        """
        """

        def factors(a1):
            for v1 in range(1, a1 + 1):
                if v1 * v1 > a1:
                    break
                if a1 % v1:
                    continue
                yield v1
                if a1 // v1 != v1:
                    yield (a1 // v1)

        def check(a1):

            def count(a1):
                v1 = [0] * 26
                for v2 in range(a1, a1 + a1):
                    v1[ord(a1[v2]) - ord('a')] += 1
                return v1
            v1 = count(0)
            return all((count(i) == v1 for v2 in range(a1, len(a1), a1)))
        return min((l for v1 in factors(len(a1)) if check(v1)))
