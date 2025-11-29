class C1(object):

    def findSubsequences(self, a1):
        """
        """

        def findSubsequencesHelper(a1, a2, a3, a4):
            if len(a3) >= 2:
                a4.append(list(a3))
            v1 = set()
            for v2 in range(a2, len(a1)):
                if (not a3 or a1[v2] >= a3[-1]) and a1[v2] not in v1:
                    v1.add(a1[v2])
                    a3.append(a1[v2])
                    findSubsequencesHelper(a1, v2 + 1, a3, a4)
                    a3.pop()
        v1, v2 = ([], [])
        findSubsequencesHelper(a1, 0, v2, v1)
        return v1
