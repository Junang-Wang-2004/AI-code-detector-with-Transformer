class C1(object):

    def removeInvalidParentheses(self, a1):
        """
        """

        def findMinRemove(a1):
            v1, v2 = (0, 0)
            for v3 in a1:
                if v3 == '(':
                    v1 += 1
                elif v3 == ')':
                    if not v1:
                        v2 += 1
                    else:
                        v1 -= 1
            return (v1, v2)

        def isValid(a1):
            sum = 0
            for v1 in a1:
                if v1 == '(':
                    sum += 1
                elif v1 == ')':
                    sum -= 1
                if sum < 0:
                    return False
            return sum == 0

        def removeInvalidParenthesesHelper(a1, a2, a3):
            if a2 == 0 and a3 == 0:
                v1 = ''
                for v2, v3 in enumerate(a1):
                    if v2 not in removed:
                        v1 += v3
                if isValid(v1):
                    res.append(v1)
                return
            for v2 in range(a1, len(a1)):
                if a3 == 0 and a2 > 0 and (a1[v2] == '('):
                    if v2 == a1 or a1[v2] != a1[v2 - 1]:
                        removed[v2] = True
                        removeInvalidParenthesesHelper(v2 + 1, a2 - 1, a3)
                        del removed[v2]
                elif a3 > 0 and a1[v2] == ')':
                    if v2 == a1 or a1[v2] != a1[v2 - 1]:
                        removed[v2] = True
                        removeInvalidParenthesesHelper(v2 + 1, a2, a3 - 1)
                        del removed[v2]
        v1, v2 = ([], {})
        v3, v4 = findMinRemove(a1)
        removeInvalidParenthesesHelper(0, v3, v4)
        return v1
