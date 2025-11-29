class C1(object):

    def findEvenNumbers(self, a1):
        """
        """
        v1 = 3

        def backtracking(a1, a2, a3):
            if len(a1) == v1:
                a3.append(reduce(lambda x, y: x * 10 + y, a1))
                return
            for v1, v2 in enumerate(a2):
                if v2 == 0 or (not a1 and v1 == 0) or (len(a1) == v1 - 1 and v1 % 2 != 0):
                    continue
                a2[v1] -= 1
                a1.append(v1)
                backtracking(a1, a2, a3)
                a1.pop()
                a2[v1] += 1
        v2 = [0] * 10
        for v3 in a1:
            v2[v3] += 1
        v4 = []
        backtracking([], v2, v4)
        return v4
