class C1:

    def letterCasePermutation(self, a1):
        v1 = []

        def backtrack(a1, a2):
            if a1 == len(a1):
                v1.append(''.join(a2))
                return
            v1 = a1[a1]
            if v1.isalpha():
                a2.append(v1.lower())
                backtrack(a1 + 1, a2)
                a2.pop()
                a2.append(v1.upper())
                backtrack(a1 + 1, a2)
                a2.pop()
            else:
                a2.append(v1)
                backtrack(a1 + 1, a2)
                a2.pop()
        backtrack(0, [])
        return v1
