class C1(object):

    def letterCasePermutation(self, a1):
        """
        """
        v1 = [[]]
        for v2 in a1:
            if v2.isalpha():
                for v3 in range(len(v1)):
                    v1.append(v1[v3][:])
                    v1[v3].append(v2.lower())
                    v1[-1].append(v2.upper())
            else:
                for v4 in v1:
                    v4.append(v2)
        return list(map(''.join, v1))
