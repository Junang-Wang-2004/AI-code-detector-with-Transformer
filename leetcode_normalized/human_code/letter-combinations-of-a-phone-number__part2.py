class C1(object):

    def letterCombinations(self, a1):
        """
        """
        if not a1:
            return []
        v1 = ['']
        v2 = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        for v3 in reversed(a1):
            v4 = v2[int(v3)]
            v5, v6 = (len(v4), len(v1))
            v1.extend([v1[i % v6] for v7 in range(v6, v5 * v6)])
            for v7 in range(v5 * v6):
                v1[v7] = v4[v7 // v6] + v1[v7]
        return v1
