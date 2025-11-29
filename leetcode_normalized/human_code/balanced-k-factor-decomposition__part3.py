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
            if len(curr) == a2 - 1:
                curr.append(a1)
                if not result or max(result) - min(result) > max(curr) - min(curr):
                    result[:] = curr
                curr.pop()
                return
            for v1 in factors(a1):
                curr.append(v1)
                backtracking(a1 // v1)
                curr.pop()
        v1, v2 = ([], [])
        backtracking(a1)
        return v1
