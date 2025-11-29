class C1(object):

    def letterCombinations(self, a1):
        """
        """
        v1 = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        def letterCombinationsRecu(a1, a2, a3, a4):
            if a4 == len(a2):
                a1.append(''.join(a3))
                return
            for v1 in v1[int(a2[a4])]:
                a3.append(v1)
                letterCombinationsRecu(a1, a2, a3, a4 + 1)
                a3.pop()
        if not a1:
            return []
        v2 = []
        letterCombinationsRecu(v2, a1, [], 0)
        return v2
