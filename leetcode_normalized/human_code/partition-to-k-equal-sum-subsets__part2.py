class C1(object):

    def canPartitionKSubsets(self, a1, a2):
        """
        """

        def dfs(a1, a2, a3, a4):
            if a3 == len(a1):
                return True
            for v1 in range(len(a4)):
                if a4[v1] + a1[a3] > a2:
                    continue
                a4[v1] += a1[a3]
                if dfs(a1, a2, a3 + 1, a4):
                    return True
                a4[v1] -= a1[a3]
                if not a4[v1]:
                    break
            return False
        v1 = sum(a1)
        if v1 % a2 != 0 or max(a1) > v1 // a2:
            return False
        a1.sort(reverse=True)
        v2 = [0] * a2
        return dfs(a1, v1 // a2, 0, v2)
