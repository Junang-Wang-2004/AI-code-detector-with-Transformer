class C1(object):

    def findLongestWord(self, a1, a2):
        """
        """
        a2.sort(key=lambda x: (-len(x), x))
        for v1 in a2:
            v2 = 0
            for v3 in a1:
                if v2 < len(v1) and v1[v2] == v3:
                    v2 += 1
            if v2 == len(v1):
                return v1
        return ''
