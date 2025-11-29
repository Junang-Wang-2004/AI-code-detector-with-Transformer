class C1(object):

    def addOperators(self, a1, a2):
        v1 = []

        def dfs(a1, a2, a3, a4):
            if a1 == len(a1):
                if a2 == a2:
                    v1.append(''.join(a4))
                return
            v1 = 0
            for v2 in range(a1, len(a1)):
                v1 = v1 * 10 + int(a1[v2])
                if a1[a1] == '0' and v2 > a1:
                    break
                v3 = str(v1)
                if a1 == 0:
                    a4.append(v3)
                    dfs(v2 + 1, v1, v1, a4)
                    a4.pop()
                else:
                    a4.append('+')
                    a4.append(v3)
                    dfs(v2 + 1, a2 + v1, v1, a4)
                    a4.pop()
                    a4.pop()
                    a4.append('-')
                    a4.append(v3)
                    dfs(v2 + 1, a2 - v1, -v1, a4)
                    a4.pop()
                    a4.pop()
                    a4.append('*')
                    a4.append(v3)
                    v4 = a2 - a3 + a3 * v1
                    v5 = a3 * v1
                    dfs(v2 + 1, v4, v5, a4)
                    a4.pop()
                    a4.pop()
        dfs(0, 0, 0, [])
        return v1
