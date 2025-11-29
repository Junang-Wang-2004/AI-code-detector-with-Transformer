class C1(object):

    def minDifference(self, a1, a2):
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

        def backtracking(a1):
            v1 = curr[-1] if curr else 1
            if len(curr) == a2 - 1 and a1 >= v1:
                curr.append(a1)
                if not result or result[-1] - result[0] > curr[-1] - curr[0]:
                    result[:] = curr
                curr.pop()
                return
            for v2 in factors(a1):
                if v2 < v1:
                    continue
                curr.append(v2)
                backtracking(a1 // v2)
                curr.pop()
        v1, v2 = ([], [])
        backtracking(a1)
        return v1
