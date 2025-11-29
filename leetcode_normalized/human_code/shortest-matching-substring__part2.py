class C1(object):

    def shortestMatchingSubstring(self, a1, a2):
        """
        """
        v1 = float('inf')

        def getPrefix(a1):
            v1 = [-1] * len(a1)
            v2 = -1
            for v3 in range(1, len(a1)):
                while v2 + 1 > 0 and a1[v2 + 1] != a1[v3]:
                    v2 = v1[v2]
                if a1[v2 + 1] == a1[v3]:
                    v2 += 1
                v1[v3] = v2
            return v1
        v2, v3, v4 = a2.split('*')
        v5 = len(a1)
        v6, v7, v8 = (len(v2), len(v3), len(v4))
        v9 = getPrefix(v2 + '#' + a1)
        v10 = getPrefix(v3 + '#' + a1)
        v11 = getPrefix(v4 + '#' + a1)
        v12 = v1
        v13 = v14 = v15 = 0
        while v13 + v7 + v8 < v5:
            while v13 < v5 and v9[v6 + 1 + v13] + 1 != v6:
                v13 += 1
            if v13 == v5:
                break
            while v14 < v5 and (not (v14 >= v13 + v7 and v10[v7 + 1 + v14] + 1 == v7)):
                v14 += 1
            if v14 == v5:
                break
            while v15 < v5 and (not (v15 >= v14 + v8 and v11[v8 + 1 + v15] + 1 == v8)):
                v15 += 1
            if v15 == v5:
                break
            v12 = min(v12, v15 - (v13 - v6))
            v13 += 1
        return v12 if v12 != v1 else -1
