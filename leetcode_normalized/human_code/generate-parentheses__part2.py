class C1(object):

    def generateParenthesis(self, a1):
        """
        """

        def generateParenthesisRecu(a1, a2, a3, a4):
            if a1 == 0 and a2 == 0:
                a4.append(''.join(a3))
            if a1 > 0:
                a3.append('(')
                generateParenthesisRecu(a1 - 1, a2, a3, a4)
                a3.pop()
            if a1 < a2:
                a3.append(')')
                generateParenthesisRecu(a1, a2 - 1, a3, a4)
                a3.pop()
        v1 = []
        generateParenthesisRecu(a1, a1, [], v1)
        return v1
