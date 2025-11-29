class C1(object):

    def equationsPossible(self, a1):
        """
        """
        v1 = [[] for v2 in range(26)]
        for v3 in a1:
            v4 = ord(v3[0]) - ord('a')
            v5 = ord(v3[3]) - ord('a')
            if v3[1] == '!':
                if v4 == v5:
                    return False
            else:
                v1[v4].append(v5)
                v1[v5].append(v4)
        v6 = [None] * 26
        v7 = 0
        for v8 in range(26):
            if v6[v8] is not None:
                continue
            v7 += 1
            v9 = [v8]
            while v9:
                v10 = v9.pop()
                for v11 in v1[v10]:
                    if v6[v11] is not None:
                        continue
                    v6[v11] = v7
                    v9.append(v11)
        for v3 in a1:
            if v3[1] != '!':
                continue
            v4 = ord(v3[0]) - ord('a')
            v5 = ord(v3[3]) - ord('a')
            if v6[v4] is not None and v6[v4] == v6[v5]:
                return False
        return True
