class C1(object):

    def canPartitionKSubsets(self, a1, a2):
        """
        """

        def dfs(a1, a2, a3, a4, a5):
            if a5[a3] is None:
                v1 = (a4 - 1) % a2 + 1
                a5[a3] = any((dfs(a1, a2, a3 | 1 << i, a4 - num, a5) for v2, v3 in enumerate(a1) if a3 >> v2 & 1 == 0 and v3 <= v1))
            return a5[a3]
        v1 = sum(a1)
        if v1 % a2 or max(a1) > v1 // a2:
            return False
        v2 = [None] * (1 << len(a1))
        v2[-1] = True
        return dfs(a1, v1 // a2, 0, v1, v2)
