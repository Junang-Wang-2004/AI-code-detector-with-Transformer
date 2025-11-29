class C1(object):

    def letterCombinations(self, a1):
        """
        """
        if not a1:
            return []
        v1 = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        v2 = 1
        for v3 in a1:
            v2 *= len(v1[int(v3)])
        v4 = []
        for v5 in range(v2):
            v6, v7 = (v2, [])
            for v3 in a1:
                v8 = v1[int(v3)]
                v6 //= len(v8)
                v7.append(v8[v5 // v6 % len(v8)])
            v4.append(''.join(v7))
        return v4
