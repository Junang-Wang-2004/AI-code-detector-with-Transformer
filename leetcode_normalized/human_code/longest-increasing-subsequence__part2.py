class C1(object):

    def lengthOfLIS(self, a1):
        """
        """
        v1 = []

        def insert(a1):
            v1, v2 = (0, len(v1) - 1)
            while v1 <= v2:
                v3 = v1 + (v2 - v1) // 2
                if v1[v3] >= a1:
                    v2 = v3 - 1
                else:
                    v1 = v3 + 1
            if v1 == len(v1):
                v1.append(a1)
            else:
                v1[v1] = a1
        for v2 in a1:
            insert(v2)
        return len(v1)
