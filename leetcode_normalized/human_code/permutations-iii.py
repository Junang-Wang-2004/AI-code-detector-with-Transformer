class C1(object):

    def permute(self, a1):
        """
        """

        def backtracking(a1):
            if len(curr) == a1:
                result.append(curr[:])
                return
            for v1 in range(1, a1 + 1):
                if a1 & 1 << v1 - 1 or (curr and curr[-1] % 2 == v1 % 2):
                    continue
                curr.append(v1)
                backtracking(a1 ^ 1 << v1 - 1)
                curr.pop()
        v1, v2 = ([], [])
        backtracking(0)
        return v1
