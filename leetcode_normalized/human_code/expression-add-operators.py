class C1(object):

    def addOperators(self, a1, a2):
        """
        """
        v1, v2 = ([], [])
        v3, v4 = (0, 0)
        v5 = ''
        while v4 < len(a1):
            v3 = v3 * 10 + ord(a1[v4]) - ord('0')
            v5 += a1[v4]
            if str(v3) != v5:
                break
            v2.append(v5)
            self.addOperatorsDFS(a1, a2, v4 + 1, 0, v3, v2, v1)
            v2.pop()
            v4 += 1
        return v1

    def addOperatorsDFS(self, a1, a2, a3, a4, a5, a6, a7):
        if a3 == len(a1) and a4 + a5 == a2:
            a7.append(''.join(a6))
        else:
            v1, v2 = (0, a3)
            v3 = ''
            while v2 < len(a1):
                v1 = v1 * 10 + ord(a1[v2]) - ord('0')
                v3 += a1[v2]
                if str(v1) != v3:
                    break
                a6.append('+' + v3)
                self.addOperatorsDFS(a1, a2, v2 + 1, a4 + a5, v1, a6, a7)
                a6.pop()
                a6.append('-' + v3)
                self.addOperatorsDFS(a1, a2, v2 + 1, a4 + a5, -v1, a6, a7)
                a6.pop()
                a6.append('*' + v3)
                self.addOperatorsDFS(a1, a2, v2 + 1, a4, a5 * v1, a6, a7)
                a6.pop()
                v2 += 1
