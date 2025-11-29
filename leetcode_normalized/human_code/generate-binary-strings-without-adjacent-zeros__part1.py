class C1(object):

    def validStrings(self, a1):
        """
        """

        def backtracking(a1):
            if a1 == a1:
                result.append(''.join(curr))
                return
            if not curr or curr[-1] == '1':
                curr.append('0')
                backtracking(a1 + 1)
                curr.pop()
            curr.append('1')
            backtracking(a1 + 1)
            curr.pop()
        v1, v2 = ([], [])
        backtracking(0)
        return v1
